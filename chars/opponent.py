from chars.char import Characters
from random import *
from chars.monsters import *
from chars.char_creation import player
from supporting.game_obj import *
class Opponent(Characters):
    def __init__(self, name, lvl, max_hp, hp, attack_bonus, damage, ac, exp):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, damage, ac)
        self.exp = exp
   
    def enemy_appear(self):
        monsters_list = [goblin, skeleton, orc_bandit, wyvern, void_demon]
        if player.lvl < 3:
            op = choice(monsters_list[:1])
        elif player.lvl < 5:
            op = choice(monsters_list[:-3])
        elif player.lvl < 7:
            op = choice(monsters_list[:-2])
        elif player.lvl < 9:
            op = choice(monsters_list[:-1])
        else:
            op = choice(monsters_list)
        self.name = op.name
        self.lvl = player.lvl + randint(-1, 1)
        if self.lvl < 1:
            self.lvl = 1
        elif self.lvl > 10:
            self.lvl = 10
        self.max_hp = round(player.max_hp*op.max_hp * (1 + (self.lvl - player.lvl)*0.1) * game.difficult)
        self.hp = self.max_hp
        self.attack_bonus = round(op.attack_bonus*self.lvl*game.difficult)
        self.damage = op.damage
        self.damage[1] = round(self.damage[1]*game.difficult)
        self.damage[2] = round(self.damage[2]*(1+(self.lvl-op.alvl)*0.2)*game.difficult)
        self.ac = round(op.ac * player.ac * (1 + (self.lvl - player.lvl)*0.1)*game.difficult)
        self.exp = round(self.lvl*op.exp*game.difficult)
        print_slow(f"Your opponent is {self.name}, lvl: {self.lvl}. ")

enemy = Opponent("name", 1, 1, 1, 1, [1, 2, 1], 1, 1)
    

