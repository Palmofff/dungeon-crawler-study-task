from equipment.armor import *
from equipment.weapons import *
from random import *
from chars.char_creation import player
from utils.defs import *

armor_dict = {
    "1-2": [leather],
    "3-4": [iron],
    "5-6": [adamantine],
    "7-8": [dragon],
    "9-10": [demonic],
}

weapon_dict = {
    "1-2": [battleaxe, scimitar, sickle],
    "3-4": [shortsword, maul, war_pick],
    "5-6": [lance, rapier],
    "7-8": [longsword, greatsword],
    "9-10": [halebard, greataxe],
}
answers = ["Yes", "No"]


def chest():
    awr = randint(1, 2)
    if awr == 1:
        choice_lvl = player.lvl - int(not player.lvl % 2)
        armor_by_level = armor_dict[f"{choice_lvl}-{choice_lvl+1}"]
        armor_generated = choice(armor_by_level)
        print_slow(
            f"You get {armor_generated.name}, lvl: {armor_generated.lvl}, armor class: {armor_generated.ac}."
        )
        print_slow(
            f"You use {player.armor.name}, lvl: {player.armor.lvl}, armor class: {player.armor.ac}."
        )
        input_slow("Want to equip new armor from chest? Yes/No:")
        arm_ans = input().capitalize()
        while arm_ans not in answers:
            input_slow("Answer only Yes, or No: ")
            arm_ans = input().capitalize()
        if arm_ans == "Yes":
            player.ac -= player.armor.ac
            player.armor = armor_generated
            player.ac += player.armor.ac
            print_slow(f"You equipped {player.armor.name}.")
    elif awr == 2:
        choice_lvl = player.lvl - int(not player.lvl % 2)
        weapons_by_level = weapon_dict[f"{choice_lvl}-{choice_lvl+1}"]
        weapon_generated = choice(weapons_by_level)
        print_slow(
            f"You get {weapon_generated.name}. Lvl:{weapon_generated.lvl}, Attack bonus: {weapon_generated.attack_bonus},\
Damage: {weapon_generated.damage[0]}d{weapon_generated.damage[1]}+{weapon_generated.damage[2]}"
        )
        print_slow(
            f"You use {player.weapon.name}. Lvl:{player.weapon.lvl}, Attack bonus: {player.weapon.attack_bonus},\
Damage: {player.weapon.damage[0]}d{player.weapon.damage[1]}+{player.weapon.damage[2]}"
        )
        input_slow("Want to equip new weapon from chest? Yes/No:")
        wep_ans = input().capitalize()
        while wep_ans not in answers:
            input_slow("Answer only Yes, or No: ")
            wep_ans = input().capitalize()
        if wep_ans == "Yes":
            player.attack_bonus -= player.weapon.attack_bonus
            player.weapon = weapon_generated
            player.damage = player.weapon.damage
            player.attack_bonus += player.weapon.attack_bonus
            print_slow(f"You equipped {player.weapon.name}.")
