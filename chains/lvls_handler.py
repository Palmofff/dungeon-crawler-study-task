from chains.abstracthandler import *
from supporting.lvlup import *
class Lvls(AbstractHandler):
    def handle(self, request):
        lvl_up()
        return super().handle(request)