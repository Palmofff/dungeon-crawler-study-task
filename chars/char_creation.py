from chars.hero import *
from random import *
from equipment.armor import *
from equipment.weapons import *
from chars.races import *
from supporting.defs import *
from supporting.game_obj import *
player = Hero("name", "race", 1, 1, 1, 1, [1, 5, 1], 1, 0, 0, sickle, leather)

def create_char():
        input_slow("Give a name to your char:")
        player.name = input()
        player.lvl = 1
        print_slow("You can choose a race from this list: human, elf, dwarf, orc")
        racelist = {"human":human, "elf":elf, "dwarf":dwarf, "orc":orc}
        input_slow("Choose your race:")
        race_choose = input()
        while race_choose not in racelist:
            print_slow("Error, choose race only from list given below!")
            input_slow("Choose your race:")
            race_choose = input()
        player.race = racelist[race_choose] 

        player.armor = leather
        player.ac = player.race.ac + player.armor.ac
        print_slow(f"Your starting armor is {player.armor.name}")

        input_slow("You can choose your starting weapon from this list:battleaxe, scimitar, sickle:")
        weap_choose = input()
        weap_list = {"battleaxe":battleaxe, "scimitar":scimitar, "sickle":sickle}
        while weap_choose not in weap_list:
            print_slow("Error! Choose only from list given  below!")
            input_slow("You can choose your starting weapon from this list:battleaxe, scimitar, sickle:")
            weap_choose = input()
        player.weapon = weap_list[weap_choose]
        print_slow(f"Your starting weapon is {player.weapon.name}")
        player.attack_bonus = player.race.attack_bonus + player.weapon.attack_bonus
        print_slow(f"Your attack bonus is {player.attack_bonus}")
        player.damage = player.weapon.damage
        print_slow(f"Your damage is {player.damage[0]}d{player.damage[1]}+{player.damage[2]} ")

        player.max_hp = randint(11, 18)
        player.hp = player.max_hp
        print_slow(f"Your hp is {player.hp}/{player.max_hp}")
        player.exp = 0
        player.score = 0
        game.progress = True
        print_slow("You walked in forest and then you found a strange cave.")
        print_slow("You entered this cave and it was a magical portal to the labyrinth.")
        print_slow("You heard a whisper in your head:You can't go back, try to survive.*laughing*")