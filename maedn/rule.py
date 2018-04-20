from board import get_postion


class BaseRule(object):

    def check(self, move, board, player, pieces):
        """A rule takes a move, the board and the list of pieces and return a sublist of
        those pieces that are allowed to move according to the rule. So a list of pieces
        can be passed on to several rules and will be reduced if needed

        :param move: A Move instance
        :param board: A Board instance
        :param pieces: A list of pieces
        :return: A list of pieces
        """
        return pieces


class OtherPieceCanThrowOut(BaseRule):
    """ If a piece can throw out another piece, other move are not allowed
    The german term for this is Rausschmeisspflicht
    """

    def check(self, move, board, player, pieces):
        players_pieces = board.board_state[player]
        other_pieces = []

        for p, i in enumerate(board.board_state):
            if i == player:
                continue

            for piece in p:
                other_pieces.append(piece)

        allowed_pieces = [p for p in players_pieces if (p + move) in other_pieces]

        return allowed_pieces or pieces


class EmptyBasePositionFirst(BaseRule):
    pass
