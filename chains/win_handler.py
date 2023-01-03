from chains.abstracthandler import *
from chars.char_creation import player
from chars.boss import *

class Finish_game(AbstractHandler):
     def handle(self, request):
        if end_boss.defeated == True:
            if mid_boss.defeated == True:
                player.score = round((player.score+player.exp)*1.2)
            player.score = round(player.score*1.5)
            print_slow("You finished this game! Thank you for playing my first game!")
            print_slow(f"Your score is {player.score}")
        else:
            return super().handle(request)


