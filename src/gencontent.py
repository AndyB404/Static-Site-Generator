import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Error: No header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, "r")
    content = f.read()
    f.close()
    t = open(template_path, "r")
    template = t.read()
    t.close()
    HTMLNode = markdown_to_html_node(content)
    HTMLString = HTMLNode.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", HTMLString)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    out = open(dest_path, "w")
    out.write(template)
    out.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if entry.endswith(".md"):
            generate_page(source_path, template_path, Path(dest_path).with_suffix(".html"))
        else:
            generate_pages_recursive(source_path, template_path, dest_path)


