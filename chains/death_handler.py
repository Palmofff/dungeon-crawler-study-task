from chains.abstracthandler import *
from chars.char_creation import player
from supporting.defs import *
from supporting.game_obj import *
from chars.boss import *
class Death(AbstractHandler):
    def handle(self, request):
        if player.hp <= 0:
            if mid_boss.defeated == True:
                player.score =  round((player.score+player.exp)*1.2)
            print_slow("You died.")
            print_slow(f"Your score is {player.score}. Game wasn't finished, try again.")
            game.progress = False
        else:
            return super().handle(request)

