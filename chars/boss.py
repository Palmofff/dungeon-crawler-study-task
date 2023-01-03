from chars.monsters import *
from chars.char_creation import *
from chars.char import *


class Bosses(Characters):
    def __init__(self, name, lvl, max_hp, hp, attack_bonus, damage, ac, defeated):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, damage, ac )
        self.defeated = defeated
        self.damage = damage
        

    def mid_boss_appear(self):
        mid_boss.max_hp = player.max_hp
        mid_boss.hp = mid_boss.max_hp
        mid_boss.attack_bonus = player.attack_bonus
        mid_boss.damage = player.damage
        mid_boss.ac = player.ac
        print_slow("You entered big room with a mirror.\
As soon as you saw a reflection of yourself, it crawled out of the mirror and rushed at you. ")
        
    def end_boss_appear(self):
        end_boss.max_hp = round(1.5*player.max_hp)
        end_boss.hp = end_boss.max_hp
        end_boss.ac = round(player.ac*1.2)
        print_slow("You entered a huge space with a portal at the end.\
The portal is guarded by a massive ancient dragon. You will become dragon's meal, if you can't win.")
                

mid_boss = Bosses("mirror demon", 5, 1, 1, 1, 1, 1, False)
end_boss = Bosses("ancient dragon", 10, 1.5, 1.5, 4, [1, 12, 4], 1.2, False )