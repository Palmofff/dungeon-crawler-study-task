from chars.opponent import *
from random import *
from chars.char_creation import *
from utils.defs import *
from chars.boss import *

act_lst = ["run", "fight"]


def attack(atacker, atacked):
    attack_result = randint(1, 20)
    is_crit = True if attack_result == 20 else False
    damage = 1
    if attack_result + atacker.attack_bonus >= atacked.ac:
        damage = roll_damage(atacker.damage[0], atacker.damage[1], atacker.damage[2])
        if is_crit:
            damage *= 2
            print_slow("Critical attack!")
        if damage >= atacked.hp:
            damage = atacked.hp
        atacked.hp -= damage
        print_slow(f"{atacker.name} dealt {damage} to {atacked.name}")
        print_slow(f"{atacked.name} hp is {atacked.hp}/{atacked.max_hp}")
    else:
        print_slow(f"{atacker.name} missed")


def roll_damage(dice_count, dice_value, damage_bonus):
    dice_results = []
    for _ in range(dice_count):
        dice_results.append(randint(1, dice_value))
    return sum(dice_results) + damage_bonus


def fight():
    while player.hp > 0 and enemy.hp > 0:
        j = input("You want to fight, or run: ")
        while j not in act_lst:
            j = input("Error, choose only from:run, or fight:")
        if j == "run" and not enemy.isboss:
            break
        elif j == "run" and enemy.name == "mirror demon":
            print_slow("Door is locked, you can't run.")
        elif j == "run" and enemy.name == "ancient dragon":
            print_slow("It's no door here anymore, only dragon and portal.")
        elif j == "fight":
            if player.hp > 0 and enemy.hp > 0:
                attack(player, enemy)
                if enemy.hp <= 0 and not enemy.isboss:
                    print_slow(f"You killed {enemy.name} and gained {enemy.exp} exp.")
                    player.exp += enemy.exp
                    print_slow(f"Your exp is {player.exp}")
                elif enemy.hp <= 0 and enemy.name == mid_boss.name:
                    mid_boss.defeated = True
                elif enemy.hp <= 0 and enemy.name == end_boss.name:
                    end_boss.defeated = True
            if player.hp > 0 and enemy.hp > 0:
                attack(enemy, player)
