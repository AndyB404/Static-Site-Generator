import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md = "# this is a title"
        title = extract_title(md)
        self.assertEqual(title, "this is a title")

    def test_extract_title_multiple_lines(self):
        md = """
this is some text
# this is a title
this is more text
"""
        title = extract_title(md)
        self.assertEqual(title,"this is a title")

    def test_extract_title_no_header(self):
        md = "just text here"
        with self.assertRaises(Exception):
            extract_title(md)