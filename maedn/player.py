from maedn.strategy import MoveFirst
from maedn.strategy import BaseStrategy
from maedn.dice import StandardDice
import random


class Player(object):
    strategy = None

    def __init(self, strategy: BaseStrategy = MoveFirst, dice=StandardDice):
        self.strategy = strategy
        self.dice = dice

    def get_next_move(self, board, dice_roll):
        return self.strategy.get_next_move(board)

    def roll(self) -> int:
        return self.dice.roll()
