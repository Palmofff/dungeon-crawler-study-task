from chains.abstracthandler import *
from supporting.defs import *
from chars.char_creation import player
from chars.boss import *
from supporting.fight import *
class EndBoss(AbstractHandler):
    def handle(self, request):
        if player.lvl >= 10 and end_boss.defeated == False :
            Bosses.end_boss_appear(end_boss)
            end_boss_fight()
        else:
            return super().handle(request)