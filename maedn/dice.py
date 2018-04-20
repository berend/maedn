import random


class StandardDice(object):

    def __init__(self):
        self.randomizer = random.SystemRandom()

    def roll(self) -> int:
        return self.randomizer.choice(1, 2, 3, 4, 5, 6)


class BetterDice(StandardDice):

    def roll(self) -> int:
        return self.randomizer.choice(1, 2, 3, 4, 5, 5, 6, 6)
