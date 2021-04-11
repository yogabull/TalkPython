"""This is my attempt to create the weather app."""

import requests


def main():
    print_header()
    user_location = get_user_location()
    location = unpack_user_location(user_location)
    # weather = request_location_weather(location)
    # report_weather()


def print_header():
    print("-------------------------")
    print("      Weather App")
    print("-------------------------")


def get_user_location():
    user_location = input(
        'Where do you want to know the weather? [City, ST, Country] ')
    print(f'You selected: {user_location}.')
    return user_location.rstrip().lower()


def unpack_user_location(loc):
    print(type(loc))
    print(loc)
    loc = loc.split(',')
    print(loc, type(loc))
    print(loc[0])
    print(loc[1])


def request_location_weather(location):
    pass


def report_weather():
    pass


main()

if __name__ == "__main___":
    main()
