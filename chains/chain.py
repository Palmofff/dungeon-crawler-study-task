from chains.handler1 import *
from chains.abstracthandler import *
from chains.death_handler import *
from chains.win_handler import *
from chains.lvls_handler import*
from chains.endboss_handler import *
from chains.midboss_handler import*
from chains.lab_handler import *
from chars.char_creation import player
def chained(handler: Handler):
    handler.handle(player)


death = Death()
finish = Finish_game()
lvls = Lvls()
endb = EndBoss()
mdb = Midboss()
labyrinth = Labyrinth()

death.set_next(finish).set_next(lvls)
lvls.set_next(endb).set_next(mdb)
mdb.set_next(labyrinth)