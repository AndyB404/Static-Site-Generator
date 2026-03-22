import os, shutil
from copystatic import source_to_destination
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    source_to_destination(dir_path_static, dir_path_public)
    generate_pages_recursive("content", "template.html", "public")

main()


       