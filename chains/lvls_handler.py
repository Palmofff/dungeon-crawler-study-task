from chains.abstracthandler import *
from utils.lvlup import *


class Lvls(AbstractHandler):
    def handle(self, request):
        lvl_up()
        return super().handle(request)
