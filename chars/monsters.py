from chars.char import Characters
class Monsters(Characters):
    def __init__(self, name, lvl, max_hp, hp,  attack_bonus, ac, damage, exp):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, ac)
        self.damage = damage
        self.exp = exp