"""Weather App Ex05 - Michael Kennedy tutorials"""


def main():
    """ Get location for weather"""
    show_header() # Displays app header.
    location_text = input(
        "Where do you want the weather report (ex. Dallas, USA)? ")
    # print(f"You selected {location_text}. \n")
    print("You selected %d. \n", location_text)

    """Convert plain text request to data we can use"""
    city, state, country = convert_plaintext_location(location_text)
    print(city, state, country)

    # Get report from the weather api
    # report returned weather data


def convert_plaintext_location(location_text):
    """Clean location string."""
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
        """Assigns input to variables."""
        city = parts[0]
        state = parts[1]
        country = parts[2]
    else:
        return None

    # loc = city, state, country  # creates a tuple object.
    return city, state, country


def show_header():
    """App Header"""
    print('---------------------------')
    print('      Weather Client')
    print('---------------------------')
    print()


if __name__ == "__main__":
    main()
