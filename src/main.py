import os, shutil, sys
from copystatic import source_to_destination
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1] 
    else:
        basepath = "/"
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    source_to_destination(dir_path_static, dir_path_public)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()


       