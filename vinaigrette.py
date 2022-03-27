import random
import time
import datetime

"""
Reads two dates in form YYYY-MM-DD, draw new date between them.
If the new date is Monday, the program will print "I don't have vinaigrette".
dates example: 2022-3-14 is Monday
2022-3-13
2022-3-15
"""


def random_date(start_date: str, end_date: str, time_format: str, random_number: random) -> datetime:
    """
    The function parses the strings start_date and end_end to struct_time then,
    converts them to float, multiplies by random and converts it to local time.
    :param start_date: Start date in form YYYY-MM-DD.
    :param end_date: End date in form YYYY-MM-DD.
    :param time_format: Time format of start and end. for example
    %Y-%m-%d, %m/%d/%Y %I:%M %p etc.
    :param random_number: Random number to adding to start.
    :return: Date representing by '2022-3-16'.
    """
    start_time = time.mktime(time.strptime(start_date, time_format))
    end_time = time.mktime(time.strptime(end_date, time_format))

    ptime = start_time + random_number * (end_time - start_time)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)


def vinaigrette():
    """
    Reads two dates from user, and draws new date between them.
    If the new date is Monday, the function will print "I don't have Vinaigrette".
    """
    monday = 0

    start_date = input("Enter a start date\n")
    end_date = input("Enter a end date\n")

    date_between_start_to_end = random_date(start_date, end_date, '%Y-%m-%d', random.random())

    if date_between_start_to_end.weekday() == monday:
        print("monday")


if __name__ == '__main__':
    vinaigrette()
