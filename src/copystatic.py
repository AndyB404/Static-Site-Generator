import os, shutil

def source_to_destination(source, destination):
    if os.path.isfile(source):     
        print(f"* {source} -> {destination}")
        shutil.copy(source, destination)
    if os.path.isdir(source):
        os.mkdir(destination)
        contents = os.listdir(source)
        for content in contents:
            from_path = os.path.join(source, content)
            dest_path = os.path.join(destination, content)
            source_to_destination(from_path, dest_path)