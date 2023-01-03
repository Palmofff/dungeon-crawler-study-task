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
                lw = input()
                while lw not in labway or lw == "right":
                    input_slow("Error, choose only from left, straight:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "straight":
                    game.difficult = 0.8
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 35:
                        chest()
                    elif 36 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                elif lw == "left":
                    game.difficult = 0.6
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 30:
                        chest()
                    elif 31 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
        elif lw == "straight":
            game.difficult = 0.8
            if 1 <= way_r <= 25:
                chest()
            elif 26 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lw = input()
                while lw not in labway or lw == "straight":
                    input_slow("Error, choose only from left, right:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "right":
                    game.difficult = 1
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 45:
                        chest()
                    elif 46 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                elif lw == "left":
                    game.difficult = 0.6
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 30:
                        chest()
                    elif 31 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
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
                lw = input()
                while lw not in labway or lw == "left":
                    input_slow("Error, choose only from straight, right:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "right":
                    game.difficult = 1
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 45:
                        chest()
                    elif 46 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                if lw == "straight":
                    game.difficult = 0.8
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 35:
                        chest()
                    elif 36 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()


        return super().handle(request)