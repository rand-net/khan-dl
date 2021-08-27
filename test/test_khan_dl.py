import unittest
import youtube_dl
import sys

sys.path.append("../khan_dl")
from khan_dl.khan_dl import *


class TestKhanDL(unittest.TestCase):
    def test_get_courses(self):
        print("test_get_courses")
        khan_dl = KhanDL()
        courses, courses_url = khan_dl.get_courses("https://www.khanacademy.org/math")
        self.assertIsNotNone(courses)
        self.assertIsNotNone(courses_url)
        self.assertEqual(len(courses), len(courses_url))

    def test_get_course_page(self):
        print("test_get_course_page")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/precalculus"
        khan_dl.get_course_page()
        self.assertIsNotNone(khan_dl.course_page)

    def test_get_course_title(self):
        print("test_get_course_title")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/precalculus"
        khan_dl.get_course_page()
        khan_dl.get_course_title()
        self.assertEqual(khan_dl.course_title, "Precalculus")

    def test_get_course_unit_urls(self):
        print("test_get_course_unit_urls")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/precalculus"
        khan_dl.get_course_page()
        khan_dl.get_course_unit_urls()
        self.assertEqual(len(khan_dl.course_unit_urls), 10)

    def test_get_course_unit_titles(self):
        print("test_get_course_unit_titles")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/precalculus"
        khan_dl.get_course_page()
        khan_dl.get_course_unit_titles()
        self.assertIsNotNone(khan_dl.course_unit_titles)
        self.assertEqual(len(khan_dl.course_unit_titles), 10)

    def test_get_course_unit_slugs(self):
        print("test_get_course_unit_slugs")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/precalculus"
        khan_dl.get_course_page()
        khan_dl.get_course_title()
        khan_dl.get_course_unit_titles()
        khan_dl.get_course_unit_slugs()
        self.assertEqual(len(khan_dl.course_unit_slugs), 10)

    def test_youtube_dl_down_playlist(self):
        print("test_youtube_dl_down_playlist")
        course_unit_url = (
            "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:complex"
        )
        lesson_youtube_ids = []
        youtube_dl_opts = {}
        with youtube_dl.YoutubeDL(youtube_dl_opts) as ydl:
            info_dict = ydl.extract_info(course_unit_url, download=False)
            for video in info_dict["entries"]:
                video_id = video.get("id", None)
                lesson_youtube_ids.append(video_id)

        self.assertIsNotNone(lesson_youtube_ids)
        self.assertEqual(len(lesson_youtube_ids), 22)

    def test_lesson_title_match_youtube_ids(self):
        print("test_lesson_title_match_youtube_ids")
        khan_dl = KhanDL()
        khan_dl.course_url = "https://www.khanacademy.org/math/trigonometry"
        khan_dl.get_course_page()
        khan_dl.get_course_title()
        khan_dl.get_course_unit_titles()
        khan_dl.get_course_unit_slugs()
        khan_dl.get_course_unit_urls()
        khan_dl.get_course_all_slugs()
        khan_dl.get_course_youtube_ids()
        self.assertEqual(len(khan_dl.course_all_slugs), len(khan_dl.lesson_youtube_ids))


if __name__ == "__main__":
    unittest.main()
