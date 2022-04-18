import logging
import logging.handlers
from .khan_dl import *
import argparse
import sys
from art import tprint

__version__ = "1.2.5"


def set_log_level(args):
    if not args.verbose:
        logging.basicConfig(level=logging.ERROR)
    elif int(args.verbose) == 1:
        logging.basicConfig(level=logging.WARNING)
    elif int(args.verbose) == 2:
        logging.basicConfig(level=logging.INFO)
    elif int(args.verbose) >= 3:
        logging.basicConfig(level=logging.DEBUG)


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
        "-c",
        "--course_url",
        help="Enter Course URL",
    )

    argparser.add_argument(
        "-a",
        "--all",
        help="Download all Courses from all Domains",
        action="store_true",
    )

    argparser.add_argument(
        "-v",
        "--verbose",
        help="Verbose Levels of log. 1 = Warning; 2 = Info; 3 = Debug",
    )

    args = argparser.parse_args()

    if args.interactive_prompt:
        set_log_level(args)
        tprint("KHAN-DL")
        khan_down = KhanDL()
        khan_down.download_course_interactive()

    elif args.course_url:
        set_log_level(args)
        tprint("KHAN-DL")
        print("Looking up " + args.course_url + "...")
        selected_course_url = args.course_url
        khan_down = KhanDL()
        khan_down.download_course_given(selected_course_url)

    elif args.all:
        set_log_level(args)
        tprint("KHAN-DL")
        khan_down = KhanDL()
        all_course_urls = khan_down.get_all_courses()
        for course_url in all_course_urls:
            khan_down.download_course_given(course_url)
