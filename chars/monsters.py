from char import Characters
class Monsters(Characters):
    def __init__(self, name, race, lvl, attack, ac, damage, exp):
        super().__init__(name, race, lvl, attack, ac)
        self.damage = damage
        self.exp = exp