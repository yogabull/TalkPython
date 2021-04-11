def main():
    d = {
        'city': 'Dallas',
        'state': 'Texas',
        'country': 'DE',
        'details': ['Cold', 'Snowy', 'Wintery']
    }

    # print(d.get('country', 'USA'))
    # d['country'] = 'AU'
    # print(d.get('country', 'USA'))
    # d['planet'] = 'Earth'
    # print(d.get('planet'))
    # print(d)

    w = {
        "weather": {
            "description": "broken clouds",
            "category": "Clouds"
        },
        "wind": {
            "speed": 8.05,
            "deg": 310
        },
        "units": "imperial",
        "forecast": {
            "temp": 56.73,
            "feels_like": 53.65,
            "pressure": 1024,
            "humidity": 33,
            "low": 55,
            "high": 57
        },
        "location": {
            "city": "Portland",
            "state": "OR",
            "country": "US"
        },
        "rate_limiting": {
            "unique_lookups_remaining": 49,
            "lookup_reset_window": "1 hour"
        }
    }

    print(w.get('forecast').get('temp'))
    print(w.get('forecast').get('low'))
    print(w.get('location').get('city'))


if __name__ == "__main__":
    main()
