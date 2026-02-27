import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_text_not_equal(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_equal_text(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text1", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text1", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_url_equal(self):
        node = TextNode("text1", TextType.BOLD, "https://example.com")
        node2 = TextNode("text1", TextType.BOLD, "https://example.com")
        self.assertEqual(node, node2)

    def test_url_not_equal(self):
        node = TextNode("text1", TextType.BOLD, "https://example1.com")
        node2 = TextNode("text1", TextType.BOLD, "https://example2.com")
        self.assertNotEqual(node, node2)

    def test_text_type_not_equal(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text1", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    


if __name__ == "__main__":
    unittest.main()