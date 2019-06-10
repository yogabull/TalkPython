# redo exercise that asks for birth date, and returns how many passed since birthday or number of days until birthday.

import datetime

def header():
    print('---------------------------')
    print('       Birthday App')
    print('---------------------------\n')


def get_birthday():
    name = input('What is your name? ')
    year = int(input('What year were you born [YYYY]: '))
    month = int(input('What month were you born [MM]: '))
    day = int(input('What day were you born [DD]: '))
    print(f'{name}, you were born {month}/{day}/{year}')
    birthday = datetime.date(year,month,day)
    return birthday, name

def calculate_number_of_days(birthday): #returns number of days between bday and today.
    now = datetime.date.today()
    #NOTE: next line changes birth date year to this year.
    this_year_bday = datetime.date(now.year, birthday.month, birthday.day)
    timedelta = this_year_bday - now
    #NOTE: the next line changes timedelta to a integer from a datetime class.
    number = timedelta.days
    return number


def message(name, number):
    if number < 0:
        print(f'{name}, your birthday was {-number} days ago.')
    elif number > 0:
        print(f'{name}, your birthday is in {number} days.')
    elif number == 0:
        print(f'Happy Birthday, {name}')
    print()


def main():
    header()
    bday, name = get_birthday()
    number = calculate_number_of_days(bday)
    message(name, number)


main()
