# redo exercise that asks for birth date, and returns how many passed since birthday or number of days until birthday.

import datetime

def header():
    print('---------------------------')
    print('       Birthday App')
    print('---------------------------')


def get_birthday():
    name = input('What is your name? ')
    year = int(input('What year were you born [2019]: '))
    month = int(input('What month were you born [01]: '))
    day = int(input('What day were you born [01]: '))
    print(f'{name}, you were born {month}/{day}/{year}')
    bday = datetime.date(year,month,day)
    return bday, name

def calculate_number_of_days(birthday):
    now = datetime.date.today()
    print(f'The date today is {now}', type(now))
    number_days = birthday - now
    number = number_days.days
    print(f'Number_days [{number_days}] has the class ', type(number_days))
    print(f'This is converted to the number {number} which now has the class ', type(number))
    print('Converting the datetime class to and integer lets us do math.\n')
    # print('the difference is ', number_days, type(number_days))
    # print(number, type(number))
    return(number)


def message(name, number_days):
    print(name)
    number = number_days.days
    print(number, type(number))
    if number < 0:
        print(f'{name}, your birthday was {-number} days ago.')
    elif number > 0:
        print(f'{name}, your birthday is in {number} days.')
    elif number == 0:
        print(f'Happy Birthday, {name}')


def main():
    header()
    # bday = get_birthday()
    name = 'john'
    bday = datetime.date(2019, 6, 1)
    # print(f'The date we are using is {bday}')
    number = calculate_number_of_days(bday)
    # message(name, number)


main()
