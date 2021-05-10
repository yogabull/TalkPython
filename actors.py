"""D&D module for constructing creatures."""


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'This is a level {self.level} {self.name}. '


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'A {self.name} of level {self.level}. '
