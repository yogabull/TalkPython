# working through exercise with less help.
# 5/26 needed lots of help, but understanding is much improved.

import datetime

def print_header():
    print('----------------------------')
    print('      Birthday Machine')
    print('----------------------------')
    print()


def get_user_birthday():
    # name = input('What is your name? ')
    # print('When were you born {}?'.format(name))
    year = 1971
    # year = int(input('Year [YYYY]: '))
    month = int(input('What month [MM]: '))
    day = int(input('What day [DD]: '))
    birthday = datetime.date(year, month, day)
    # print(type(birthday))
    # print('Hi {}, your birthday is {}.'.format(name, birthday))
    return birthday


def compute_days_between_dates(today, bdate):
    this_year = datetime.date(year = today.year, month = bdate.month, day = bdate.day)
    dt = today - this_year # created is the class 'datetime.timedelta'. Not an integer.
    return dt.days #this method turns the dt class to an integer.
    # these print statements output classes for verificaiton.
    # print(today, type(today))
    # print(bdate, type(bdate))
    # print(dt, type(dt))
    # print(dt.days, type(dt.days))


def print_birthday_information(number_of_days):
    if number_of_days < 0:
        print('Your birthday is in {} days.'.format(-number_of_days))
    elif number_of_days > 0:
        print('Your birthday was {} days ago.'.format(number_of_days))
    else:
        print('Happy Birthday.')


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(today, bday)
    print_birthday_information(number_of_days)


main()
