import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
        node2 = TextNode("text1", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example1.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://example1.com"})

    def test_image(self):
        node = TextNode("", TextType.IMAGE, "https://example1.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example1.com", "alt": ""})


if __name__ == "__main__":
    unittest.main()