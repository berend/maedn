from maedn.game import Game
from maedn.player import Player

player_one = Player()
player_two = Player()
player_three = Player()
player_four = Player()


game = Game(player_one, player_two, player_three, player_four)

while not game.is_ended:
    game.next_move()
