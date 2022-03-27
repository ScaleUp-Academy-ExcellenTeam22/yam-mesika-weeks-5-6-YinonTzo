import os

"""
This module implements function to
find files are start with "deep" in some file.

For more explanations about listdir:
https://www.tutorialspoint.com/python/os_listdir.htm.
"""


def open_path(path_name: str) -> list:
    """
    :param path_name: Path name to open.
    :return:List with all dirs inside @path_name.
    """
    return os.listdir(path_name)


def extract_names_startswith_deep(dirs_name: list) -> list:
    """
    :param dirs_name: List with dirs name.
    :return: Files are start with "deep".
    """
    return [file for file in dirs_name if file.startswith("deep")]


def print_names_startswith_deep(path: str) -> None:
    """
    Prints the name are start with deeps.
    :param path: File to open to find names.
    """
    dirs = open_path(path)
    deeps = extract_names_startswith_deep(dirs)
    print(deeps)


if __name__ == '__main__':
    path_to_open = "D:\\yam-mesika-weeks-5-6-YinonTzo\\images"

    print_names_startswith_deep(path_to_open)
