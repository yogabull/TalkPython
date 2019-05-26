# working through exercise with less help.

import datetime

def print_header():
    print('----------------------------')
    print('      Birthday Machine')
    print('----------------------------')
    print()


def get_user_birthday():
    name = input('What is your name? ')
    print('When were you born {}?'.format(name))
    year = int(input('Year [YYYY]: '))
    month = int(input('What month [MM]: '))
    day = int(input('What day [DD]: '))
    birthday = datetime.date(year, month, day)
    print(type(birthday))
    print('Hi {}, your birthday is {}.'.format(name, birthday))

def compute_days_between_dates():
    bday_this_year = datetime.date()
#
#
# def print_birthday_information():
#     pass


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    # number_of_days = compute_days_between_dates(bday, today)
    # print_birthday_information(number_of_days)
    print('Nearly done.')


main()
