import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Invalid markdown: delimiter not closed")
            for part in range(0, len(parts)):
                if parts[part] == "":
                    continue
                if part % 2 == 0:
                    new_node = TextNode(parts[part], TextType.TEXT)
                    new_nodes.append(new_node)
                else:
                    new_node = TextNode(parts[part], text_type)
                    new_nodes.append(new_node)
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        extracted_images = extract_markdown_images(node.text)
        for img in extracted_images:
            image_markdown = f"![{img[0]}]({img[1]})"
            sections = current_text.split(image_markdown, 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        extracted_links = extract_markdown_links(node.text)
        for lnk in extracted_links:
            link_markdown = f"[{lnk[0]}]({lnk[1]})"
            sections = current_text.split(link_markdown, 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(lnk[0], TextType.LINK, lnk[1]))
            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

