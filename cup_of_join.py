
def join(*lists: list, seperator: str = '-') -> list or None:
    """
    :param lists: List of lists.
    :param seperator: Seperator to be between the lists.
    :return: New list with combination of lists with seperator between each list.
    """
    if not lists:
        return None

    return [li for sublist in lists for li in sublist + list(seperator)][:-1]


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], seperator='@'))

