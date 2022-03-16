import random
import time
import datetime


def random_date(start, end, time_format, random_number):
    """
    The function parses the strings start and end to struct_time
    then, converts them to float, multiplies by random
    and converts it to local time.
    :param start:
    :param end:
    :param time_format: time format of start and end. for example
    %Y-%m-%d, %m/%d/%Y %I:%M %p etc
    :param random_number: random number to adding to start
    :return: date representing by '2022-3-16'
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + random_number * (etime - stime)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)


def vinaigrette():
    """
    Reads two dates from user, and draws new date between them.
    if the new date is Monday, the function prints "I don't have Vinaigrette"
    :return: None
    """
    MONDAY = 0

    start = input("Enter a start date\n")
    end = input("Enter a end date\n")

    new_date = random_date(start, end, '%Y-%m-%d', random.random())

    if new_date.weekday() == MONDAY:
        print("monday")


"""
dates example: 2022-3-14 is Monday
2022-3-13
2022-3-15
"""
if __name__ == '__main__':
    vinaigrette()
