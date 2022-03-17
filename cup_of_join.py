def join(*lists: list, sep='-'):
    """

    :param lists: list of lists
    :param sep: seperator
    :return: new list with combination of lists with seperator between each
    two list
    """
    if not lists:
        return None

    ret = []
    for li in lists:
        ret += li
        ret += sep

    return ret[:-1:]


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
