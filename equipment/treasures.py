from equipment.armor import *
from equipment.weapons import *
from random import *
from chars.char_creation import player
from supporting.defs import *
armor_list = [leather, iron, adamantine, dragon, demonic]
weapon_list = [battleaxe, scimitar, sickle, shortsword, maul, war_pick, lance, 
rapier, longsword, greatsword, halebard, greataxe]
answers = ["Yes", "No"]
def chest():
    awr = randint(1, 2)
    if awr == 1:
        if player.lvl < 3:
            armor_choice = choice(armor_list[:1])
        elif player.lvl < 5:
            armor_choice = choice(armor_list[:2])
        elif player.lvl < 7:
            armor_choice = choice(armor_list[:3])
        elif player.lvl < 9:
            armor_choice = choice(armor_list[:-1])
        else:
             armor_choice = choice(armor_list)  
        print_slow(f"You get {armor_choice.name}, lvl: {armor_choice.lvl}, armor class: {armor_choice.ac}.")
        print_slow(f"You use {player.armor.name}, lvl: {player.armor.lvl}, armor class: {player.armor.ac}.")
        input_slow("Want to equip new armor from chest? Yes/No:")
        arm_ans = input()
        while arm_ans not in answers:
            input_slow("Answer only Yes, or No: ")
            arm_ans = input()
        if arm_ans == "Yes":
            player.ac -= player.armor.ac
            player.armor = armor_choice
            player.ac += player.armor.ac
            print_slow(f"You equipped {player.armor.name}.")
    elif awr == 2:
        if player.lvl < 3:
            weapon_choice = choice(weapon_list[:3])
        elif player.lvl < 5:
            weapon_choice = choice(weapon_list[:6])
        elif player.lvl < 7:
            weapon_choice = choice(weapon_list[:8])  
        elif player.lvl < 9:
            weapon_choice = choice(weapon_list[:-2])
        else:
            weapon_choice = choice(weapon_list)       
        print_slow(f"You get {weapon_choice.name}. Lvl:{weapon_choice.lvl}, Attack bonus: {weapon_choice.attack_bonus},\
Damage: {weapon_choice.damage[0]}d{weapon_choice.damage[1]}+{weapon_choice.damage[2]}")
        print_slow(f"You use {player.weapon.name}. Lvl:{player.weapon.lvl}, Attack bonus: {player.weapon.attack_bonus},\
Damage: {player.weapon.damage[0]}d{player.weapon.damage[1]}+{player.weapon.damage[2]}")
        input_slow("Want to equip new weapon from chest? Yes/No:")
        wep_ans = input()
        while wep_ans not in answers:
            input_slow("Answer only Yes, or No: ")
            wep_ans = input()
        if wep_ans == "Yes":
            player.attack_bonus -= player.weapon.attack_bonus
            player.weapon = weapon_choice
            player.damage = player.weapon.damage
            player.attack_bonus += player.weapon.attack_bonus
            print_slow(f"You equipped {player.weapon.name}.")
    