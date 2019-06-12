import os


def count_files(dir):
    # get relative path from the absolute path
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = os.path.join(abs_path, dir)

    # get text files
    files = []
    for r, d, f in os.walk(rel_path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    # print the list of text files (path)
    # for f in files:
    #     print(f)

    # print the file count
    print('\n' + str(len(files)) + ' files need to be processed')
