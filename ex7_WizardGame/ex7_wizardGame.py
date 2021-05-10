"""D and D game"""

from actors import Creature, Wizard
import random
import time


def main():
    print_title()
    game_loop()


def game_loop():
    creatures = [
        Creature('Toad', '1'),
        Creature('Snake', '5'),
        Creature('Tiger', '50'),
        Creature('Dragon', '500'),
        Creature('Evil Wizard', '1000'),
    ]

    hero = Wizard('Gandolf', '75')

    while True:
        active_creature = random.choice(creatures)

        print(
            f'\nA {active_creature.name} of level {active_creature.level} has emerged from the fog.')

        cmd = input(
            'Do you want to [a] attack, [l] look around, [r] run away?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)

        elif cmd == 'l':
            print(f"\n{hero} sees:")
            for i in creatures:
                print("   a", i)
        elif cmd == 'r':
            pass
        else:
            print('Looks like you are done. Bye.')
            break


def print_title():
    print('-----------------------------')
    print('       Dungeon Game')
    print('-----------------------------')
    print()


if __name__ == '__main__':
    main()
