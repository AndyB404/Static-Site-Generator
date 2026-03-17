from enum import Enum
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        cleaned = block.strip()
        if cleaned != "":
            stripped_blocks.append(cleaned)
    return stripped_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(mdtext):
    heading = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    quote = (">", "> ")
    lines = mdtext.split("\n")
    line_number = 1
    if mdtext.startswith(heading):
        return BlockType.HEADING
    if mdtext.startswith("```\n") and mdtext.endswith("```"):
        return BlockType.CODE
    if mdtext.startswith(quote):
        for line in lines:
            if not line.startswith(quote):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if mdtext.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if mdtext.startswith(f"{line_number}. "):
        for line in lines:
            if not line.startswith(f"{line_number}. "):
                return BlockType.PARAGRAPH
            line_number += 1 
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is BlockType.HEADING:
            marker = block.split(" ")[0]
            level = len(marker)
            header_tag = f"h{level}" 
            header_text = block.split(" ", 1)[1]
            children.append(ParentNode(header_tag, text_to_children(header_text)))
        elif block_type is BlockType.PARAGRAPH:
            paragraph_text = block.replace("\n", " ")
            children.append(ParentNode("p", text_to_children(paragraph_text)))
        elif block_type is BlockType.CODE:
            code_text = block[4:-3]
            converted = text_node_to_html_node(TextNode(code_text, TextType.TEXT))
            code_node = ParentNode("code", [converted])
            pre_node = ParentNode("pre", [code_node])
            children.append(pre_node)
        elif block_type is BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ul", items))
        elif block_type is BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line.split(". ", 1)[1]
                items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ol", items))
        elif block_type is BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = []
            for line in lines:
                if line.startswith("> "):
                    text = line[2:]
                else:
                    text = line[1:]
                cleaned.append(text)
            quote_text = " ".join(cleaned)
            children.append(ParentNode("blockquote", text_to_children(quote_text)))
    return ParentNode("div", children)


