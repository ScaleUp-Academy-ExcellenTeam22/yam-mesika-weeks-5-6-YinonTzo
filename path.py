import os

"""
This module implements function to
find files are start with "deep" in some file

for more explanations about listdir
https://www.tutorialspoint.com/python/os_listdir.htm
"""


def open_path(path_name):
    """
    :param path_name:
    :return:list with all dirs inside @path_name
    """
    return os.listdir(path_name)


def extract_names_startswith_deep(dirs_name):
    """
    :param dirs_name: list with dirs name
    :return: files are start with "deep"
    """
    return [file for file in dirs_name if file.startswith("deep")]


def print_names_startswith_deep(path):
    """
    Prints the name are start with deeps
    :param path:
    :return:
    """
    dirs = open_path(path)
    deeps = extract_names_startswith_deep(dirs)
    print(deeps)


if __name__ == '__main__':
    path = """C:\\Users\\tzomi\\source"""
    print_names_startswith_deep(path)
