from chains.abstracthandler import *
from supporting.defs import *
from chars.char_creation import player
from chars.boss import *
from supporting.fight import *
labway = ["left", "straight", "right"]

class Midboss(AbstractHandler):
    def handle(self, request):
        if player.lvl == 5 and mid_boss.defeated == False:
            print_slow("In the right passage you can see a door...")
            input_slow("Where you want to go: right, straight or left:")
            enb_lab  = input()
            while enb_lab not in labway:
                input_slow("Error, choose only from left, straight, right :")
                enb_lab  = input()
            if enb_lab not in labway[:-1]:
                Bosses.mid_boss_appear(mid_boss)
                mid_boss_fight()
            else:
                print_slow("You found nothing...")
                mid_boss.defeated = None
        else:
            return super().handle(request)
            