from enum import Enum

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