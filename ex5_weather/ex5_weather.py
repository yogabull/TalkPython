"""
Weather App Ex05 - Michael Kennedy tutorials
This file includes using Named Tuples instead of unpacking plain tuples.

Notice the 'collections' import.
This module enables 'Location' to become a named tuple.
"""
import collections
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel('INFO')

Location = collections.namedtuple('Location', 'city state country')


def main():
    """ Here is a string. """
    show_header()

    # Get location for weather
    location_text = input(
        "Where do you want the weather report (ex. Dallas, USA)? ")
    print(f"You selected {location_text}. \n")
    # LOGGER.info(f"You selected {location_text}.")
    LOGGER.info("You selected %d.", location_text)

    loc = convert_plaintext_location(location_text)
    print(f"Using the named tuple'Location': {loc}")
    print(f"This line uses the city dot method for 'Location': {loc.city}")

    print()
    city, state, country = convert_plaintext_location(location_text)
    print('This next line uses the tuple unpacked into strings.')
    print(city, state, country)

    # Get report from the weather api
    data = call_weather_api(loc)
    print(data)

    # report returned weather data


def call_weather_api(loc):
    """ Adds state to the url if entered."""
    url = f'https://weather.talkpython.fm/api/weather?city \
        ={loc.city}&country={loc.country}&units=imperial'
    if loc.state:
        url += f'&state={loc.state}'
    print(f"\nCall this {url}")
    return url


def convert_plaintext_location(location_text):
    """ Cleans up location text."""
    if not location_text or not location_text.strip():
        return None

    location_text = location_text.lower().strip()
    parts = location_text.split(',')

    city = ''
    state = ''
    country = 'us'
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        state = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0]
        state = parts[1]
        country = parts[2]
    else:
        return None

    """Illustration of calling a tuple (t) versus calling the tuple as a named collection (t2)."""
    # t = city, state, country
    # t[0]
    # t2 = Location(city, state, country)
    # t2.city
    """The named tuple is better than plain tuples"""

    return Location(city, state, country)
    # return city, state, country


def show_header():
    """Prints header"""
    print('---------------------------')
    print('      Weather Client')
    print('---------------------------')
    print()

if __name__ == "__main__":
    main()
