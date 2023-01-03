from chars.char_creation import *
from supporting.defs import *
from random import *
from chars.hero import *
def lvl_up():
    if player.lvl < 10 and player.exp >= 69800:
        player.max_hp += randint(1, 10)*(10-player.lvl)
        player.hp = player.max_hp
        player.lvl = 10
        print_slow("Lvl up! Your lvl is 10.")
        Hero.stats(player)
    elif player.lvl < 9 and player.exp >= 48200:
        player.max_hp += randint(1, 10)*(9-player.lvl)
        player.hp = player.max_hp
        player.lvl = 9
        print_slow("Lvl up! Your lvl is 9.")
        Hero.stats(player)
    elif player.lvl < 8 and player.exp >= 35000:    
        player.max_hp += randint(1, 10)*(8-player.lvl)
        player.hp = player.max_hp
        player.lvl = 8
        print_slow("Lvl up! Your lvl is 8.")
        Hero.stats(player)
    elif player.lvl < 7 and player.exp >= 23600:
        player.max_hp += randint(1, 10)*(7-player.lvl)
        player.hp = player.max_hp
        player.lvl = 7
        print_slow("Lvl up! Your lvl is 7.")
        Hero.stats(player)
    elif player.lvl < 6 and player.exp >= 14600:
        player.max_hp += randint(1, 10)*(6-player.lvl)
        player.hp = player.max_hp
        player.lvl = 6
        print_slow("Lvl up! Your lvl is 6.")
        Hero.stats(player)
    elif player.lvl < 5 and player.exp >= 7100:
        player.max_hp += randint(1, 10)*(5-player.lvl)
        player.hp = player.max_hp
        player.lvl = 5
        print_slow("Lvl up! Your lvl is 5.")
        Hero.stats(player)
    elif player.lvl < 4 and player.exp >= 3500:
        player.max_hp += randint(1, 10)*(4-player.lvl)
        player.hp = player.max_hp
        player.lvl = 4
        print_slow("Lvl up! Your lvl is 4.")
        Hero.stats(player)
    elif player.lvl < 3 and player.exp >= 1700:
        player.max_hp += randint(1, 10)*(3-player.lvl)
        player.hp = player.max_hp
        player.lvl = 3
        print_slow("Lvl up! Your lvl is 3.")
        Hero.stats(player)
    elif player.lvl < 2 and player.exp >= 500:
        player.max_hp += randint(1, 10)
        player.hp = player.max_hp
        player.lvl = 2
        print_slow("Lvl up! Your lvl is 2.")
        Hero.stats(player)