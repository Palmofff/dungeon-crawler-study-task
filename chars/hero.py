from char import Characters
class Hero(Characters):
    def __init__(self, name, race, lvl, attack, ac, exp, weapon, armor):
        super().__init__(name, race, lvl, attack, ac)
        self.name = name
        self.exp = exp
        self.weapon = weapon
        self.armor = armor

player = Hero("player_name", "None", 1, 1, 1, 1, "weap", "kurtka")