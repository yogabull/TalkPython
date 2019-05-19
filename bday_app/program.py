import datetime

def print_header():
    print('--------------------------')
    print('      Birthday App')
    print('--------------------------')
    print()


def get_birthday_from_user():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    #First datetime is the module. The second .datetime is the class.
    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days # the class .days turns dt into an integer type.


def print_birthday_information(days):
    print('The class for {} is '.format(days), type(days))
    if days < 0:
        print('You had your birthday {} days ago.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days.'.format(days))
    else:
        Print('Happy Birthday!')


def main():
    print_header()
    bday = get_birthday_from_user()
    print('This is your birthday ',bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)
    print('Nearly done.')


main()
