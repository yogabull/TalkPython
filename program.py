"""
Dungeons and Dragons game.
Trying to recreate with little help.
I want to get more solid at creating modules.
I tried to run my first one without success.
"""

from actors import Creature
from actors import Wizard


def main():
    print_header()
    event_loop()


def print_header():
    print('------------------------------')
    print('    Dungeon and Dragons')
    print('------------------------------')
    print()


def event_loop():
    Creature('bird', 3)

    creatures = [
        Creature('toad', 2),
        Creature('snake', 7),
        Creature('tiger', 50),
        Creature('dragon', 500),
        Creature('evil_wizard', 1000)
    ]

    hero = Wizard('Bubba', 200)

    for i in creatures:
        print(i)

    print()
    print(hero)

    while True:

        cmd = input(
            "Do you want to [a] Attack, [l] Look around or [r] run away? ")
        cmd = cmd.lower()
        if cmd == 'a':
            print('Attack.')
            attack()
        elif cmd == 'l':
            print('Look around.')
        elif cmd == 'r':
            print('Run away.')
        else:
            print("I don't understand your input.")
            break

    print()


if __name__ == '__main__':
    main()
