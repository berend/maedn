from maedn.player import Player


class Board(object):

    def __init__(self, players=4, pieces=4, start_to_start_length=10):
        """board is represented as list of lists.
        a list of players pieces positions
        """
        self.num_players = players
        self.num_pieces = pieces
        self.start_pos = [(i + 1) * p for i, p in enumerate(range(players))]

    def move(self, player: Player, piece: int, roll: int) -> None:
        new_position = self.get_newpos(self.board_state[player][piece], roll)
        self.throw_out_at(player, new_position)
        self.board_state[player][piece] = new_position

    def throw_out_at(self, player, position):
        for p in range(self.num_players):
            if p == player:
                continue

            for i, pos in enumerate(self.board_state[p]):
                if pos == position:
                    self.board_state[p].pop(i)
                    break
