from chains.abstracthandler import *
from utils.defs import *
from chars.char_creation import player
from chars.boss import *
from utils.fight import *


class EndBoss(AbstractHandler):
    def handle(self, request):
        if player.lvl >= 10 and not end_boss.defeated:
            Opponent.end_boss_appear(enemy)
            fight()
        else:
            return super().handle(request)
