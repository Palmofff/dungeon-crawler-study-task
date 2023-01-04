from chains.abstracthandler import *
from chars.char_creation import player
from utils.defs import *
from utils.details import *
from chars.boss import *


class Death(AbstractHandler):
    def handle(self, request):
        if player.hp <= 0:
            player.score = player.exp + player.score
            if mid_boss.defeated:
                player.score = round((player.score) * 1.2)
            print_slow("You died.")
            print_slow(
                f"Your score is {player.score}. Game wasn't finished, try again."
            )
            game_exe.progress = False
        else:
            return super().handle(request)
