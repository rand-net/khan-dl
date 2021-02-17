from .khan_downloader import *
from .interactive_prompt import *
import argparse
import sys

__version__ = "0.1.4"


def download(downloader):
    downloader.get_course_html()
    downloader.generate_unit_slugs()
    downloader.generate_unit_urls()
    downloader.generate_course_slugs_video_ids()
    downloader.download_videos()


def main(argv=None):
    argv = sys.argv if argv is None else argv
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-i",
        "--interactive",
        help="Enter Interactive Course Selection Mode",
        dest="interactive_prompt",
        action="store_true",
    )
    argparser.add_argument(
        "-c", "--course_url", help="Enter Course URL",
    )

    argparser.add_argument(
        "-a",
        "--all",
        help="Download all Courses from all Domains",
        action="store_true",
    )

    args = argparser.parse_args()

    if args.interactive_prompt:
        selected_course_url = course_selection_prompt()

        khan_down = Khan_DL("", selected_course_url)
        print("Generating Path Slugs..... ")
        download(khan_down)

    elif args.course_url:
        print("Looking up " + args.course_url + " .....")
        selected_course_url = args.course_url
        khan_down = Khan_DL("", selected_course_url)

        print("Generating Path Slugs..... ")
        download(khan_down)

    elif args.all:
        print("Downloading all Courses from all Domains")
        all_course_urls = get_all_course_urls()

        for course_url in all_course_urls:

            khan_down = Khan_DL("", course_url)
            download(khan_down)
