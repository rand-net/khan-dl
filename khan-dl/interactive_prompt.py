from prompt_toolkit import prompt
from prompt_toolkit.completion import (
    WordCompleter,
    Completer,
    FuzzyWordCompleter,
)
from bs4 import BeautifulSoup
import requests

def get_all_course_urls():
    course_domains = ["Math", "Science", "Computing", "Humanities", "Economics-Finance-Domain"]
    all_course_urls = []
    for course_domain in course_domains:
        print("Processing Course Domain: ", course_domain)
        course_url_list = []
        course_list_page_url = (
            "https://www.khanacademy.org/" + course_domain.lower()
        )

        print("\nDownloading Course List...\n")
        # Download Selected Course Domain Page HTML
        course_list_page_source = requests.get(course_list_page_url).text
        course_list_page_html = BeautifulSoup(course_list_page_source, "lxml")

        for courses_header_section in course_list_page_html.find_all("h2", class_="_158q6at"):
            course_header_tag = courses_header_section.find("a", class_="_dwmetq")

            course_header = courses_header_section.find("a", class_="_dwmetq").text
            course_header_slug = course_header_tag["href"]

            course_url_list.append("https://www.khanacademy.org" + course_header_slug)
        all_course_urls.extend(course_url_list)
    return all_course_urls

def course_selection_prompt():
    # COURSE LIST URLs
    # https://www.khanacademy.org/math/
    # https://www.khanacademy.org/science/
    # https://www.khanacademy.org/computing
    # https://www.khanacademy.org/humanities
    # https://www.khanacademy.org/economics-finance-domain

    # Choose a Course Domain
    course_domain_completer = FuzzyWordCompleter(
        ["Math", "Science", "Computing", "Humanities", "Economics-Finance-Domain"]
    )
    selected_course_domain = prompt(
        "Course Domain: ", completer=course_domain_completer
    )
    print("Selected Course Domain: %s" % selected_course_domain)

    # Get a list of all the courses in the domain
    course_list = []
    course_url_list = []
    course_list_page_url = (
        "https://www.khanacademy.org/" + selected_course_domain.lower()
    )

    print("\nDownloading Course List...\n")
    # Download Selected Course Domain Page HTML
    course_list_page_source = requests.get(course_list_page_url).text
    course_list_page_html = BeautifulSoup(course_list_page_source, "lxml")

    for courses_header_section in course_list_page_html.find_all(
        "h2", class_="_158q6at"
    ):
        course_header_tag = courses_header_section.find("a", class_="_dwmetq")

        course_header = courses_header_section.find("a", class_="_dwmetq").text
        course_header_slug = course_header_tag["href"]

        course_url_list.append("https://www.khanacademy.org" + course_header_slug)
        course_list.append(course_header)

    # Choose a Course
    course_list_completer = FuzzyWordCompleter(course_list)
    selected_course = prompt("Course: ", completer=course_list_completer)
    print("\nSelected Course Domain: %s\n" % selected_course)

    # Find the selected course index and match the Course URL
    selected_course_index = course_list.index(selected_course)
    selected_course_url = course_url_list[selected_course_index]
    return selected_course_url
