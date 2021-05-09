"""Module to define creatures and hero in game."""
import random
import time


class Creature():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.name} [level {self.level}]"


class Wizard():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.name}"

    def attack(self, creature):
        print()
        print(f"{self.name} attacks the {creature.name}.")
        attack_roll = int(self.level) * random.randint(1, 12)
        defense_roll = int(creature.level) * random.randint(1, 12)
        time.sleep(3)
        print("... and ...")
        time.sleep(3)

        if attack_roll > defense_roll:
            print(f"{self.name} defeats the {creature.name}!\n")
            return True
        else:
            print(f"The {creature.name} defeats {self.name}! ...\n")
            return False
