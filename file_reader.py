import os


def get_files(dir):
    files = []
    path = get_relative_path(dir)
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    return files


def get_relative_path(dir):
    abs_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(abs_path, dir)
