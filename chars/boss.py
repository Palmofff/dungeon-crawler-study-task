from chars.monsters import *
from chars.char_creation import *
from chars.char import *
from equipment.treasures import answers


class Bosses(Characters):
    def __init__(self, name, lvl, max_hp, hp, attack_bonus, damage, ac, defeated):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, damage, ac)
        self.defeated = defeated
        self.damage = damage

    def mid_boss_reward(self):
        if self.defeated:
            print_slow(
                f"You get {dragon.name}, lvl: {dragon.lvl} armor class: {dragon.ac}."
            )
            print_slow(
                f"You use {player.armor.name}, lvl: {player.armor.lvl},\
 armor class: {player.armor.ac}."
            )
            input_slow("Wanna equip? Yes/No:")
            ar_mb = input().capitalize()
            while ar_mb not in answers:
                input_slow("Answer only Yes, or No: ")
                ar_mb = input().capitalize()
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
            print_slow(
                f"You get {rew_w.name}. Lvl:{rew_w.lvl}, Attack bonus: {rew_w.attack_bonus},\
Damage: {rew_w.damage[0]}d{rew_w.damage[1]}+{rew_w.damage[2]}"
            )
            print_slow(
                f"You use {player.weapon.name}. Lvl:{player.weapon.lvl},\
Attack bonus: {player.weapon.attack_bonus},\
Damage: {player.weapon.damage[0]}d{player.weapon.damage[1]}+{player.weapon.damage[2]}"
            )
            input_slow("Want to equip new weapon from chest? Yes/No:")
            rew_wp_ans = input().capitalize()
            while rew_wp_ans not in answers:
                input_slow("Answer only Yes, or No: ")
                rew_wp_ans = input().capitalize()
            if rew_wp_ans == "Yes":
                player.attack_bonus -= player.weapon.attack_bonus
                player.weapon = rew_w
                player.attack_bonus += player.weapon.attack_bonus
                player.damage = player.weapon.damage
                print_slow(f"You equipped {player.weapon.name}.")

    def end_boss_appear(self):
        end_boss.max_hp = round(1.5 * player.max_hp)
        end_boss.hp = end_boss.max_hp
        end_boss.ac = round(player.ac * 1.2)
        print_slow(
            "You entered a huge space with a portal at the end.\
The portal is guarded by a massive ancient dragon. You will become dragon's meal, if you can't win."
        )


mid_boss = Bosses("mirror demon", 5, 1, 1, 1, 1, 1, False)
end_boss = Bosses("ancient dragon", 10, 1.5, 1.5, 4, [1, 12, 4], 1.2, False)
