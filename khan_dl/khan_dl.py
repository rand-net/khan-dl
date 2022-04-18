import os
import platform
import requests
import sys
import logging
from yt_dlp.utils import DownloadError
import yt_dlp

from typing import List, Dict, Tuple
from bs4 import BeautifulSoup
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import ProgressBar

VIDEO_SITE_URL = "https://www.youtube.com/watch?v="
ROOT_URL = "https://www.khanacademy.org"
DOMAINS = [
    "math",
    "science",
    "computing",
    "humanities",
    "economics-finance-domain",
    "ela",
]

# Tags and attributes for parsing HTML

COURSE_HEAD = {"tag": "h2", "class": "_158q6at"}
COURSE_URL = {"tag": "a", "class": "_dwmetq"}
COURSE_TITLE = {"data-test-id": "unit-block-title"}
COURSE_UNIT_TITLE = {"data-test-id": "unit-header"}
COURSE_SUBUNIT_TITLE_ATTRS = {"data-test-id": "lesson-card-link"}
COURSE_SUBUNIT_BODY = {"tag": "ul", "class": "_37mhyh"}
COURSE_LESSON_BODY = {"tag": "div", "class_i": "_10ct3cvu", "class_ii": "_1p9458yw"}
COURSE_LESSON_SPAN = {"tag": "span", "class": "_e296pg"}
COURSE_LESSON_LABEL = "aria-label"
COURSE_LESSON_TITLE = {"tag": "span", "class": "_14hvi6g8"}

"""

Domain -> Course -> Unit Page -> Subunit Header + Subunit Block -> Lesson Block -> Lesson Title

"""


def clear_screen():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


# Youtube-dl NoLogger
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass


class KhanDL:
    def __init__(self):
        self.domain = ""
        self.course_url = ""
        self.course_title = ""
        self.course_page = ""
        self.course_unit_titles = []
        self.course_unit_slugs = []
        self.course_unit_urls = []
        self.course_all_slugs = []
        self.lesson_titles = []
        self.lesson_youtube_ids = []
        self.output_rel_path = os.getcwd() + "/"
        self.unit_ids_counter = {}
        self.unit_slugs_counter = {}

    def get_courses(self, selected_domain_url: str) -> Tuple[List[str], List[str]]:
        """Returns the list of courses on a domain"""

        courses, courses_url = [], []
        print("\nDownloading Courses...\n")
        try:
            selected_domain_page = BeautifulSoup(
                requests.get(selected_domain_url).text, "lxml"
            )
        except requests.ConnectionError as e:
            print("Error Connecting!\n", e)
            sys.exit(1)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            sys.exit(1)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            sys.exit(1)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            sys.exit(1)

        for course_header in selected_domain_page.find_all(
            COURSE_HEAD["tag"], class_=COURSE_HEAD["class"]
        ):
            course = course_header.find(
                COURSE_URL["tag"], class_=COURSE_URL["class"]
            ).text
            courses.append(course)

            course_link = course_header.find(
                COURSE_URL["tag"], class_=COURSE_URL["class"]
            )
            course_slug = course_link["href"]
            courses_url.append(ROOT_URL + course_slug)
        return courses, courses_url

    def domain_prompt(self):
        """Returns the selected domain"""

        # Domain selection prompt
        domain_completer = FuzzyWordCompleter(
            list(map(str.title, DOMAINS))
        )  # Titlecase for aesthetics
        selected_domain = DOMAINS.index(
            prompt("Domain: ", completer=domain_completer).lower()
        )

        print("Selected Domain: {}".format(DOMAINS[selected_domain]))
        self.domain = DOMAINS[selected_domain]
        logging.info("Domain Selected")

    def course_prompt(self):
        """Returns URL for the selected course"""

        selected_domain_url = ROOT_URL + "/" + self.domain
        courses, courses_url = self.get_courses(selected_domain_url)

        # Course Selection Prompt
        courses_completer = FuzzyWordCompleter(courses)
        selected_course = courses.index(prompt("Course: ", completer=courses_completer))
        print("Selected Course: {}".format(courses[selected_course]))
        self.course_url = courses_url[selected_course]
        logging.info("Course Selected")

    def get_all_courses(self) -> List[str]:
        """Returns URL for all courses"""

        print("Downloading all Courses from all Domains...")
        all_courses_url = []
        for domain in DOMAINS:
            print("Selected Domain: ", domain)
            selected_domain_url = ROOT_URL + "/" + domain
            courses, courses_url = self.get_courses(selected_domain_url)
            all_courses_url += courses_url

        return all_courses_url

    def get_course_page(self):
        """Retrieves course page html"""

        print("Course URL: {}".format(self.course_url))
        try:
            self.course_page = BeautifulSoup(requests.get(self.course_url).text, "lxml")
        except requests.ConnectionError as e:
            print("Error Connecting!\n", e)
            sys.exit(1)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            sys.exit(1)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            sys.exit(1)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print("Oops: Something Else", err)
            sys.exit(1)

    def get_course_title(self):
        """Retrieves the course title"""

        course_title = self.course_page.find(attrs=COURSE_TITLE)
        self.course_title = course_title.text.replace(" ", "_")
        logging.debug("course_title:{}".format(self.course_title))
        logging.info("Course title retrieved")

    def get_course_unit_titles(self):
        """Retrieves course unit titles"""

        for title in self.course_page.find_all(attrs=COURSE_UNIT_TITLE):
            self.course_unit_titles.append(title.text)
        logging.debug("course_unit_titles:{}".format(self.course_unit_titles))
        logging.info("Course unit titles retrieved")

    def get_course_unit_slugs(self):
        """Retrieves course unit slugs"""

        counter = 0
        for title in self.course_unit_titles:
            self.course_unit_slugs.append(
                self.course_title + "/" + str(counter) + "_" + title.replace(" ", "_")
            )
            counter += 1
        logging.debug("course_unit_slugs:{}".format(self.course_unit_slugs))
        logging.info("Course unit slugs generated")

    def get_course_unit_urls(self):
        """Retrieves course unit urls"""

        for url in self.course_page.find_all(attrs=COURSE_UNIT_TITLE):
            self.course_unit_urls.append(url["href"])
        logging.debug("course_unit_urls:{}".format(self.course_unit_urls))
        logging.info("Course unit urls retrieved")

    def get_course_all_slugs(self):
        """Generate slugs for all units"""

        unit_lessons_counter = 0
        # Unit Page -> Subunit Header + Subunit Block -> Lesson Block -> Lesson Title
        for course_unit_url, course_unit_slug in zip(
            self.course_unit_urls, self.course_unit_slugs
        ):

            unit_lessons_counter = 0
            # -> Unit Page
            try:
                course_unit_page = BeautifulSoup(
                    requests.get(ROOT_URL + course_unit_url).text, "lxml"
                )
            except requests.ConnectionError as e:
                print("Error Connecting!\n", e)
                sys.exit(1)
            except requests.exceptions.HTTPError as errh:
                print("Http Error:", errh)
                sys.exit(1)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
                sys.exit(1)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
                sys.exit(1)
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
                sys.exit(1)

            subunit_couter = 0

            # -> Subunit Header -> Subunit Block
            for course_subunit_title, course_subunit_body in zip(
                course_unit_page.find_all(attrs=COURSE_SUBUNIT_TITLE_ATTRS),
                course_unit_page.find_all(
                    COURSE_SUBUNIT_BODY["tag"], class_=COURSE_SUBUNIT_BODY["class"]
                ),
            ):

                logging.debug("course_subunit_title:{}".format(course_subunit_title))
                lesson_counter = 0
                # ->  Lesson Block
                for course_lesson_body in course_subunit_body.find_all(
                    COURSE_LESSON_BODY["tag"],
                    {
                        "class": [
                            COURSE_LESSON_BODY["class_i"],
                            COURSE_LESSON_BODY["class_ii"],
                        ]
                    },
                ):
                    course_lesson_span = course_lesson_body.find_all(
                        COURSE_LESSON_SPAN["tag"], class_=COURSE_LESSON_SPAN["class"]
                    )
                    course_lesson_aria_label = course_lesson_span[0][
                        COURSE_LESSON_LABEL
                    ]
                    logging.debug(
                        "course_lesson_aria_label:{}".format(course_lesson_aria_label)
                    )
                    # ->  Lesson Title
                    # Check whether lesson block is a video
                    if course_lesson_aria_label == "Video":
                        lesson_title = course_lesson_body.find(
                            COURSE_LESSON_TITLE["tag"],
                            class_=COURSE_LESSON_TITLE["class"],
                        )

                        logging.debug(
                            "course_lesson_title:{}".format(lesson_title.text)
                        )
                        self.lesson_titles.append(lesson_title.text)
                        self.course_all_slugs.append(
                            self.output_rel_path
                            + course_unit_slug
                            + "/"
                            + str(subunit_couter)
                            + "_"
                            + course_subunit_title.text.replace(" ", "_")
                            + "/"
                            + str(lesson_counter)
                            + "_"
                            + lesson_title.text.replace(" ", "_")
                        )

                    lesson_counter += 1
                unit_lessons_counter += lesson_counter
                subunit_couter += 1
            self.unit_slugs_counter[course_unit_url] = unit_lessons_counter
        logging.info("Course - All slugs generated")

    def get_course_youtube_ids(self):
        """Retrieves youtube id per unit"""

        with ProgressBar() as pb:
            for i, unit_url in zip(
                pb(range(len(self.course_unit_urls)), label="Collecting Youtube IDs:"),
                self.course_unit_urls,
            ):
                unit_url = ROOT_URL + unit_url
                yt_dlp_opts = {
                    "logger": MyLogger(),
                    "retries": 20,
                    "ignoreerrors:": True,
                    "skip_download": True,
                }
                with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
                    lessons_counter = 0
                    try:
                        logging.debug(
                            "Collection youtube ids for unit:{}".format(unit_url)
                        )
                        info_dict = ydl.extract_info(unit_url, download=False)
                        for video in info_dict["entries"]:
                            video_id = video.get("id", None)
                            self.lesson_youtube_ids.append(video_id)
                            lessons_counter += 1
                    except DownloadError as e:
                        logging.debug(
                            "Collection youtube ids for unit:{}".format(unit_url)
                        )
                        info_dict = ydl.extract_info(
                            unit_url, download=False, process=False
                        )
                        for video in info_dict["entries"]:
                            video_id = video.get("url", None)
                            self.lesson_youtube_ids.append(video_id)
                            lessons_counter += 1
                    except Exception as e:
                        print("Youtube-dl: An error occured!", e)
                        sys.exit(1)

                self.unit_ids_counter[unit_url] = lessons_counter

        logging.info("Course - Collected Youtube IDs")

    def download_course_videos(self):
        """Downloads Course Videos"""

        counter = 0
        number_of_videos = len(self.course_all_slugs)

        with ProgressBar() as pb:
            for i, lesson_output_file, lesson_video_id in zip(
                pb(range(len(self.lesson_youtube_ids)), label="Downloading Videos:"),
                self.course_all_slugs,
                self.lesson_youtube_ids,
            ):
                lesson_youtube_url = VIDEO_SITE_URL + lesson_video_id

                yt_dlp_opts = {
                    "logger": MyLogger(),
                    "outtmpl": lesson_output_file,
                    "retries": 20,
                }
                with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
                    logging.debug(
                        "Downloading video[{}] {} of {}:".format(
                            lesson_youtube_url, counter, number_of_videos
                        )
                    )
                    try:
                        ydl.download([lesson_youtube_url])
                        counter += 1
                    except DownloadError:
                        error_log = open("error_private_videos.txt", "a")
                        error_log.write(
                            str(
                                lesson_output_file
                                + ", "
                                + VIDEO_SITE_URL
                                + lesson_video_id
                            )
                        )
                        error_log.close()
                    except Exception as e:
                        print("Youtube-dl: An error occured!", e)
                        sys.exit(1)
                    logging.info(
                        "Course lesson video[{}]downloaded".format(lesson_video_id)
                    )
            logging.info("All course videos downloaded")

    def download_course_interactive(self):
        """Downloads the chosen course"""
        self.domain_prompt()
        self.course_prompt()
        self.get_course_page()
        self.get_course_title()
        self.get_course_unit_titles()
        self.get_course_unit_slugs()
        self.get_course_unit_urls()

        print("\nGenerating Path Slugs...\n")
        self.get_course_all_slugs()
        self.get_course_youtube_ids()
        self.download_course_videos()

    def download_course_given(self, course_url: str):
        """Downloads the given course"""
        self.course_url = course_url
        self.get_course_page()
        self.get_course_title()
        self.get_course_unit_titles()
        self.get_course_unit_slugs()
        self.get_course_unit_urls()

        print("\nGenerating Path Slugs...\n")
        self.get_course_all_slugs()
        self.get_course_youtube_ids()
        self.download_course_videos()
