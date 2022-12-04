from chars.hero import *
from chars.races import *
from equipment.armor import *
from equipment.weapons import *
from random import *

"""                      CHARACTER CREATION                    """
player = Hero("name", "race", 1, 1, 1, 1, 1, 1, 0, 0, "weapon", "armor")
player.name = input("Give a name to your char:")

print("You can choose a race from this list: human, elf, dwarf, orc")
racelist = {"human":human, "elf":elf, "dwarf":dwarf, "orc":orc}
race_choose = input("Choose your race:")
while race_choose not in racelist:
    print("Error, choose race only from list given below!")
    race_choose = input("Choose your race:")
player.race = racelist[race_choose] 

player.armor = leather
player.ac = player.race.ac + player.armor.ac
print(f"Your starting armor is {player.armor.name}")

weap_choose = input("You can choose your starting weapon from this list:battleaxe, scimitar, sickle:")
weap_list = {"battleaxe":battleaxe, "scimitar":scimitar, "sickle":sickle}
while weap_choose not in weap_list:
    print("Error! Choose only from list given  below!")
    input("You can choose your starting weapon from this list:battleaxe, scimitar, sickle:")
player.weapon = weap_list[weap_choose]
print(f"Your starting weapon is {player.weapon.name}")
player.attack_bonus = player.race.attack_bonus + player.weapon.attack_bonus
print(f"Your attack bonus is {player.attack_bonus}")
player.damage = player.weapon.damage
print(f"Your damage is {player.damage[0]}d{player.damage[1]}+{player.damage[2]} ")

player.max_hp = randint(11, 18)
player.hp = player.max_hp
print(f"Your hp is {player.hp}/{player.max_hp}")

player.stats()