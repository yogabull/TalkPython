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
    print()
    print('Your birthday will be {}.'.format(this_year))
    if dt.days < 0:
        print('Your birthday was {} days ago.' .format(dt.days))
    elif dt.days > 0:
        print('Your birthday will be in {} days.' .format(dt.days))
    else:
        Print('Happy Birthday today.')


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    print('This is your birthday ',bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print('\n', number_of_days, '\n')
    # print_birthday_information(number_of_days)

main()
