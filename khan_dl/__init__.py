from .khan_dl import *
import argparse
import sys
from art import *

__version__ = "1.0.7"


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
        tprint("KHAN-DL")
        khan_down = KhanDL()
        khan_down.download_course_interactive()

    elif args.course_url:
        tprint("KHAN-DL")
        print("Looking up " + args.course_url + "...")
        selected_course_url = args.course_url
        khan_down = KhanDL()
        khan_down.download_course_selected(selected_course_url)

    elif args.all:
        tprint("KHAN-DL")
        khan_down = KhanDL()
        all_course_urls = khan_down.get_all_courses()
        for course_url in all_course_urls:
            khan_down.download_course_selected(course_url)
