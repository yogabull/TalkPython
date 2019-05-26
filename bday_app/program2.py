# working through exercise with less help.
import datetime

def print_header():
    print('----------------------------')
    print('      Birthday Machine')
    print('----------------------------')
    print()


def get_birthday_from_user():
    name = input('What is your name? ')
    year = int(input('What year were you born? '))
    month = int(input('What month were you born? '))
    day = int(input('What day were you born? '))
    #First datetime is the module. The second .datetime is the class
    birthday = datetime.datetime(year, month, day)
    print (birthday)
    print('Hi {}, your birthday is {}.'.format(name, birthday))

def compute_days_between_dates():
    pass


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    today = None
    number_of_days = compute_days_between_dates()
    # print_birthday_information(number_of_days)


main()
