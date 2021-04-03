"""This is a birthday app exercise."""

import datetime


def main():
    print_header()
    bday = get_user_birthday()
    now = datetime.date.today()
    td = compute_user_birthday(bday, now)
    print_birthday_info(td)


def print_header():
    print('-----------------------------')
    print('        Birthday App')
    print('-----------------------------')
    print()


def get_user_birthday():
    print("When is your birthday?")
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    bday = datetime.date(year, month, day)
    return bday


def compute_user_birthday(original_date, today):
    # this_year = datetime.date(
    #     year=today.year, month=original_date.month, day=original_date.day)
    """ Refactored below."""
    this_year = datetime.date(
        today.year, original_date.month, original_date.day)
    td = this_year - today
    return td.days


def print_birthday_info(days):
    if days > 0:
        print(f"Your birthday is in {days} days.")
    elif days < 0:
        print(f"Your birtdahy was {-days} days ago.")
    else:
        print("Happy Birthday!")

    print()
    print('-----------------------------')


main()
