from chains.abstracthandler import *
from chars.char_creation import player
from supporting.game_obj import *
from supporting.defs import *
from random import *
from equipment.treasures import *
from chars.opponent import *
from supporting.fight import *
labway = ["left", "straight", "right"]
class Labyrinth(AbstractHandler):
    def handle(self, request):
        print_slow("You can see three tunnel branch: left, straight and right. Where you want to go?")
        input_slow("Your choise:")
        lw = input()
        while lw not in labway:
            input_slow("Error, choose only from left, straight, right :")
            lw = input()
        way_r = randint(1, 100)
        if lw == "right":
            game.difficult = 1
            if 1 <= way_r <= 30:
                chest()
            elif 31 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lwr = input()
                while lwr not in labway:
                    input_slow("Error, choose only from left, straight:")
                    lwr = input()
                    while lwr == "right":
                        input_slow("Its dead end, choose only from left, straight:")
                        lwr = input()

        elif lw == 0.8:
            game.difficult = 0.8
            if 1 <= way_r <= 25:
                chest()
            elif 26 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lwr = input()
                while lwr not in labway:
                    input_slow("Error, choose only from left, right:")
                    lwr = input()
                    while lwr == "straight":
                        input_slow("Its dead end, choose only from left, right:")
                        lwr = input()
        else:
            game.difficult = 0.6
            if 1 <= way_r <= 20:
                chest()
            elif 21 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lwr = input()
                while lwr not in labway:
                    input_slow("Error, choose only from right, straight:")
                    lwr = input()
                    while lwr == "right":
                        input_slow("Its dead end, choose only from right, straight:")
                        lwr = input()


        return super().handle(request)