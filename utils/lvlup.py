from chars.char_creation import *
from utils.defs import *
from random import *
from chars.hero import *


def roll_hp(
    dice_count,
    dice_value,
):
    dice_results = []
    for _ in range(dice_count):
        dice_results.append(randint(1, dice_value))
    return sum(dice_results)


def lvl_up():
    new_lvl = player.lvl
    level_up = False
    if player.lvl < 10 and player.exp >= 69800:
        new_lvl = 10
        level_up = True
    elif player.lvl < 9 and player.exp >= 48200:
        new_lvl = 9
        level_up = True
    elif player.lvl < 8 and player.exp >= 35000:
        new_lvl = 8
        level_up = True
    elif player.lvl < 7 and player.exp >= 23600:
        new_lvl = 7
        level_up = True
    elif player.lvl < 6 and player.exp >= 14600:
        new_lvl = 6
        level_up = True
    elif player.lvl < 5 and player.exp >= 7100:
        new_lvl = 5
        level_up = True
    elif player.lvl < 4 and player.exp >= 3500:
        new_lvl = 4
        level_up = True
    elif player.lvl < 3 and player.exp >= 1700:
        new_lvl = 3
        level_up = True
    elif player.lvl < 2 and player.exp >= 500:
        new_lvl = 2
        level_up = True

    if level_up:
        player.max_hp += roll_hp((new_lvl - player.lvl), 10)
        player.hp = player.max_hp
        player.lvl = new_lvl
        print_slow(f"Lvl up! Your lvl is {player.lvl}.")
        Hero.stats(player)
