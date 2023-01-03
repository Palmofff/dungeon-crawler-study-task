from chars.char import Characters
from supporting.defs import *
class Singleton(type): 
    _instances = {} 
    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instances: 
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs) 
        return cls._instances[cls] 

class Hero(Characters, metaclass=Singleton):
    def __init__(self, name, race, lvl, max_hp, hp, attack_bonus, damage, ac, exp, score, weapon, armor):
        super().__init__(name, lvl, max_hp, hp, attack_bonus, damage, ac)
        self.name = name
        self.race = race
        self.exp = exp
        self.score = score
        self.weapon = weapon
        self.armor = armor

    def stats(self):
        print_slow(f"Name: {self.name}, race is {self.race.name}, lvl: {self.lvl}")
        print_slow(f"Armor:{self.armor.name}, Weapon: {self.weapon.name}")
        print_slow(f"Stats:Armor class:{self.ac}, Attack bonus:{self.attack_bonus}, Damage:{self.damage[0]}d{self.damage[1]}+{self.damage[2]}, HP:{self.hp}/{self.max_hp}")

        




