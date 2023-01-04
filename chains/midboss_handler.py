from chains.abstracthandler import *
from utils.defs import *
from chars.char_creation import player
from chars.boss import *
from utils.fight import *

labway = ["left", "straight", "right"]


class Midboss(AbstractHandler):
    def handle(self, request):
        if player.lvl == 5 and not mid_boss.defeated:
            print_slow("In the right passage you can see a door...")
            input_slow("Where you want to go: right, straight or left:")
            enb_lab = input()
            while enb_lab not in labway:
                input_slow("Error, choose only from left, straight, right :")
                enb_lab = input()
            if enb_lab not in labway[:-1]:
                Opponent.mid_boss_appear(enemy)
                fight()
                Bosses.mid_boss_reward(mid_boss)
            else:
                print_slow("You found nothing...")
                mid_boss.defeated = None
        else:
            return super().handle(request)
