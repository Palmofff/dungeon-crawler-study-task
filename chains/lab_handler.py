from chains.abstracthandler import *
from utils.details import game_exe
from utils.defs import *
from random import *
from equipment.treasures import *
from chars.opponent import *
from utils.fight import *
from utils.run import *

labway = ["left", "straight", "right", "stats"]


class Labyrinth(AbstractHandler):
    def handle(self, request):
        print_slow(
            "You can see three tunnel branch: left, straight and right. Where you want to go?"
        )
        print_slow("Or type stats to get your stats.")
        input_slow("Your choise:")
        lw = input()
        while lw not in labway:
            input_slow("Error, choose only from left, straight, right, or stats :")
            lw = input()
        way_r = randint(1, 100)
        if lw == "right":
            game_exe.difficult = 1
            if 1 <= way_r <= 15:
                chest()
            elif 16 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lw = input()
                while lw not in labway or lw == "right" or lw == "stats":
                    input_slow("Error, choose only from left, straight:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "straight":
                    game_exe.difficult = 0.8
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 35:
                        chest()
                    elif 36 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                elif lw == "left":
                    game_exe.difficult = 0.6
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 30:
                        chest()
                    elif 31 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
        elif lw == "straight":
            game_exe.difficult = 0.8
            if 1 <= way_r <= 10:
                chest()
            elif 11 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lw = input()
                while lw not in labway or lw == "straight" or lw == "stats":
                    input_slow("Error, choose only from left, right:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "right":
                    game_exe.difficult = 1
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 45:
                        chest()
                    elif 46 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                elif lw == "left":
                    game_exe.difficult = 0.6
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 30:
                        chest()
                    elif 31 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
        elif lw == "stats":
            Hero.stats(player)
        else:
            game_exe.difficult = 0.6
            if 1 <= way_r <= 6:
                chest()
            elif 7 <= way_r <= 95:
                Opponent.enemy_appear(enemy)
                fight()
            else:
                print_slow("Dead end, go away and try another tunnel branch")
                input_slow("What side do you want to go? Choose:")
                lw = input()
                while lw not in labway or lw == "left" or lw == "stats":
                    input_slow("Error, choose only from straight, right:")
                    lw = input()
                way_r = randint(1, 100)
                if lw == "right":
                    game_exe.difficult = 1
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 45:
                        chest()
                    elif 46 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()
                if lw == "straight":
                    game_exe.difficult = 0.8
                    way_r = randint(1, 100)
                    if 1 <= way_r <= 35:
                        chest()
                    elif 36 <= way_r <= 100:
                        Opponent.enemy_appear(enemy)
                        fight()

        return super().handle(request)
