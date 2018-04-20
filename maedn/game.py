from typing import List

from maedn.player import Player
from maedn.board import Board


class Game(object):

    def __init__(self, *players: List[Player], interval=10, pieces_per_player=4):
        self.players = players
        self.board = Board(players=len(self.players))
        """piece_position is a list with one entry for each player. Each player entry contains
        the positions of the players pieces. 
        
        0: is still at home
        >0: is on the board. Board size is defined by player size and start pos interval
        <0: is in the endzone. Endzone size defined by pieces per player
        
        """
        self.piece_position = [
            [0 for piece in range(pieces_per_player)] for player in range(self.players)
        ]

        """current_player_index: int, indicates whos turn it is, First player has index 0"""
        self.current_player_index = 0

    def next_move(self):
        reroll = False
        while reroll:
            move = self.players[self.current_player_index].roll()

            reroll = move == 6
            print(move)
            self.execute_move(move)
        self.next_player()

    def execute_move(self, move):
        pass

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    @property
    def is_ended(self):
        """
        Does any of the players have all pieces in the end zone (position<0)
        :return:
        """
        return any(
            all(pos < 0 for pos in player_positions)
            for player_positions in self.piece_position
        )
