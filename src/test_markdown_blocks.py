import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_ignore_extra_blank_lines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_one_block(self):
        md = """
This is one block of text
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is one block of text"
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\nthis is my code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">text\n> text\n>text"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- list\n- line\n- line"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. \n2. \n3. "
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "I am a paragraph\nthis is my text"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# My Heading
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>My Heading</h1></div>")

    def test_heading_level3(self):
        md = """
### My Heading
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h3>My Heading</h3></div>")

    def test_unordered_list(self):
        md = """
- item one
- item two
- item three
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>")

    def test_ordered_list(self):
        md = """
1. first
2. second
3. third
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>")

    def test_quote(self):
        md = """
> This is a quote
> that spans lines
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><blockquote>This is a quote that spans lines</blockquote></div>")

    def test_mixed_blocks(self):
        md = """
# Title

A paragraph here.

- item one
- item two
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>Title</h1><p>A paragraph here.</p><ul><li>item one</li><li>item two</li></ul></div>")