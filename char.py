class Characters:
    def __init__(self, name, race, lvl, attack, ac):
        self.name = name
        self.race = race
        self.lvl = lvl
        self.attack = attack
        self.ac = ac #ac - armor class
class Hero(Characters):
    def __init__(self, name, race, lvl, attack, ac, weapon, armor):
        super().__init__(name, race, lvl, attack, ac)
        self.weapon = weapon
        self.armor = armor
class Monster(Characters):
    def __init__(self, name, race, lvl, attack, ac, damage, exp):
        super().__init__(name, race, lvl, attack, ac)
        self.damage = damage
        self.exp = exp
        