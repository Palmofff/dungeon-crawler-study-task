from chars.char import Characters
from chars.hero import *
class Monsters(Characters):
    def __init__(self, name, alvl, lvl, max_hp, hp,  attack_bonus, ac, damage, exp):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, damage, ac)
        self.ac = ac
        self.damage = damage
        self.exp = exp
        self.alvl = alvl

goblin = Monsters("goblin", 1, 1, 0.75, 0.75, 0.3, 0.75, [1, 6, 1], 200)
skeleton = Monsters("skeleton", 3, 3, 0.8, 0.8, 0.35, 0.8, [1 , 6, 2], 300)
orc_bandit = Monsters("orc bandit", 5, 5, 0.9, 0.9, 0.35, 0.9, [1, 8, 2], 500)
wyvern = Monsters("wyvern", 7, 7, 0.9, 0.9, 0.4, 0.9, [2, 6, 3], 550 )
void_demon = Monsters("void demon", 9, 9, 1, 1, 0.45, 1, [2, 8, 3], 600)

