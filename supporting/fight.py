from chars.opponent import *
from random import *
from chars.char_creation import *
from supporting.defs import *
from chars.boss import *
from equipment.treasures import answers

act_lst = ["run", "fight"]
def fight():
    while player.hp > 0 and enemy.hp > 0:
        j = input("You want to fight, or run: ")
        while j not in act_lst:
            j = input("Error, choose only from:run, or fight:")
        if j == "run":
            break
        elif j == "fight":
            if player.hp > 0 and enemy.hp > 0:
                dice_at = randint(1, 20)+player.attack_bonus
                if dice_at >= enemy.ac:     
                    pl_dmg = (randint(player.damage[0], player.damage[1]*player.damage[0])+player.damage[2])
                    if (dice_at - player.attack_bonus) >= 20:
                        pl_dmg *= 2
                        print_slow("Critical attack!")    
                    if pl_dmg >= enemy.hp:
                        pl_dmg = enemy.hp
                    enemy.hp = enemy.hp - pl_dmg
                    player.score += pl_dmg
                    print_slow(f"You dealt {pl_dmg} damage to {enemy.name}")
                    print_slow(f"{enemy.name} hp: {enemy.hp}/{enemy.max_hp}")
                    if enemy.hp <= 0:
                        print_slow(f"You killed {enemy.name} and gained {enemy.exp} exp.")
                        player.exp += enemy.exp
                        print_slow(f"Your exp is {player.exp}")
                else: 
                    print_slow("You miss")
            if player.hp > 0 and enemy.hp > 0:
                enemy_at = randint(1, 20)+enemy.attack_bonus
                if enemy_at >= player.ac:     
                    en_dmg = (randint(enemy.damage[0], enemy.damage[1]*enemy.damage[0])+enemy.damage[2])
                    if (enemy_at - enemy.attack_bonus) >= 20:
                        en_dmg *= 2
                        print_slow("Critical attack!")    
                    if en_dmg >= player.hp:
                        en_dmg = player.hp
                    player.hp = player.hp - en_dmg
                    player.score -= en_dmg
                    print_slow(f"{enemy.name} dealt you {en_dmg} damage")
                    print_slow(f"Player hp: {player.hp}/{player.max_hp}")
                else: 
                    print_slow("You dodged enemy's attack!")


def mid_boss_fight():
    while player.hp > 0 and mid_boss.hp > 0:
        j = input("You want to fight, or run: ")
        while j not in act_lst:
            j = input("Error, choose only from:run, or fight:")
        if j == "run":
            print_slow("Door is locked, you can't run.")
        elif j == "fight":
            if player.hp > 0 and  mid_boss.hp > 0:
                dice_at = randint(1, 20)+player.attack_bonus
                if dice_at >= mid_boss.ac:
                    pl_dmg = (randint(player.damage[0], player.damage[1]*player.damage[0])+player.damage[2])
                    if (dice_at - player.attack_bonus) >= 20:
                        pl_dmg *= 2                    
                    if pl_dmg >=  mid_boss.hp:
                        pl_dmg =  mid_boss.hp
                        mid_boss.hp =  mid_boss.hp - pl_dmg
                        player.score += pl_dmg
                        print_slow(f"You dealt {pl_dmg} damage to { mid_boss.name}")
                        print_slow(f"{ mid_boss.name} hp: { mid_boss.hp}/{ mid_boss.max_hp}")
                    if  mid_boss.hp <= 0:
                        print_slow(f"You killed { mid_boss.name} and get much exp reward!")
                        player.exp = 23600
                        print_slow(f"Your exp is {player.exp}")
                        mid_boss.defeated = True
                        print_slow(f"You get {dragon.name}, lvl: {dragon.lvl} armor class: {dragon.ac}.")
                        print_slow(f"You use {player.armor.name}, lvl: {player.armor.lvl},\
 armor class: {player.armor.ac}.")
                        input_slow("Wanna equip? Yes/No:")
                        ar_mb = input()
                        while ar_mb not in answers:
                            input_slow("Answer only Yes, or No: ")
                            ar_mb = input()
                        if ar_mb == "Yes":
                            player.ac -= player.armor.ac
                            player.armor = dragon
                            player.ac += player.armor.ac
                            print_slow(f"Your new armor is {player.armor.name}")
                        rew_wp_r = randint(1, 2)
                        if rew_wp_r == 1:
                            rew_w = longsword
                        elif rew_wp_r == 2:
                            rew_w = greatsword
                        print_slow(f"You get {rew_w.name}. Lvl:{rew_w.lvl}, Attack bonus: {rew_w.attack_bonus},\
Damage: {rew_w.damage[0]}d{rew_w.damage[1]}+{rew_w.damage[2]}")
                        print_slow(f"You use {player.weapon.name}. Lvl:{player.weapon.lvl},\
Attack bonus: {player.weapon.attack_bonus},\
Damage: {player.weapon.damage[0]}d{player.weapon.damage[1]}+{player.weapon.damage[2]}")
                        input_slow("Want to equip new weapon from chest? Yes/No:")
                        rew_wp_ans = input()
                        while rew_wp_ans not in answers:
                            input_slow("Answer only Yes, or No: ")
                            rew_wp_ans = input()
                        if rew_wp_ans  == "Yes":
                            player.attack_bonus -= player.weapon.attack_bonus
                            player.weapon = rew_w.choice
                            player.attack_bonus += player.weapon.attack_bonus
                            print_slow(f"You equipped {player.weapon.name}.")
                else: 
                    print_slow("You miss")
            if player.hp > 0 and  mid_boss.hp > 0:
                enemy_at = randint(1, 20)+ mid_boss.attack_bonus
                if enemy_at >=  mid_boss.ac:     
                    en_dmg = (randint( mid_boss.damage[0],  mid_boss.damage[1]* mid_boss.damage[0])+ mid_boss.damage[2])
                    if (enemy_at - mid_boss.attack_bonus) >= 20:
                        en_dmg *= 2
                    if en_dmg >= player.hp:
                        en_dmg = player.hp
                    player.hp = player.hp - en_dmg
                    player.score -= en_dmg
                    print_slow(f"{ mid_boss.name} dealt you {en_dmg} damage")
                    print_slow(f"Player hp: {player.hp}/{player.max_hp}")
                else: 
                    print_slow("You dodged enemy's attack!")

def end_boss_fight():
     while player.hp > 0 and end_boss.hp > 0:
        j = input("You want to fight, or run: ")
        while j not in act_lst:
            j = input("Error, choose only from:run, or fight:")
        if j == "run":
            print_slow("It's no door here anymore, only dragon and portal.")
        elif j == "fight":
            if player.hp > 0 and end_boss.hp > 0:
                dice_at = randint(1, 20)+player.attack_bonus
                if dice_at >= end_boss.ac:     
                    pl_dmg = (randint(player.damage[0], player.damage[1]*player.damage[0])+player.damage[2])
                    if (dice_at - player.attack_bonus) >= 20:
                        pl_dmg *= 2
                        print_slow("Critical attack!")    
                    if pl_dmg >= end_boss.hp:
                        pl_dmg = end_boss.hp
                    end_boss.hp = end_boss.hp - pl_dmg
                    player.score += pl_dmg
                    print_slow(f"You dealt {pl_dmg} damage to {end_boss.name}")
                    print_slow(f"{end_boss.name} hp: {end_boss.hp}/{end_boss.max_hp}")
                    if end_boss.hp <= 0:
                        end_boss.defeated = True
                else: 
                    print_slow("You miss")
            if player.hp > 0 and end_boss.hp > 0:
                enemy_at = randint(1, 20)+enemy.attack_bonus
                if enemy_at >= player.ac:     
                    en_dmg = (randint(end_boss.damage[0], end_boss.damage[1]*end_boss.damage[0])+end_boss.damage[2])
                    if (enemy_at - end_boss.attack_bonus) >= 20:
                        en_dmg *= 2
                        print_slow("Critical attack!")    
                    if en_dmg >= player.hp:
                        en_dmg = player.hp
                    player.hp = player.hp - en_dmg
                    player.score -= en_dmg
                    print_slow(f"{end_boss.name} dealt you {en_dmg} damage")
                    print_slow(f"Player hp: {player.hp}/{player.max_hp}")
                else: 
                    print_slow("You dodged enemy's attack!")