class Weapon:
    def __init__(self, name, lvl, attack_bonus, damage):
        self.name = name
        self.lvl = lvl
        self.attack_bonus = attack_bonus
        self.damage = damage


battleaxe = Weapon("battleaxe", 1, 1, [1, 8, 2])  # where [1, 8, 2] is 1d8+2
scimitar = Weapon("scimitar", 1, 3, [1, 6, 1])
sickle = Weapon("sickle", 1, 5, [1, 4, 1])
shortsword = Weapon("shortsword", 3, 3, [1, 6, 2])
maul = Weapon("maul", 3, 0, [2, 6, 1])
war_pick = Weapon("war pick", 3, 2, [1, 8, 0])
lance = Weapon("lance", 5, 2, [1, 12, 0])
rapier = Weapon("rapier", 5, 4, [1, 8, 2])
longsword = Weapon("longsword", 7, 5, [1, 8, 3])
greatsword = Weapon("greatsword", 7, 2, [2, 6, 3])
halebard = Weapon("halebard", 9, 5, [1, 10, 5])
greataxe = Weapon("greataxe", 9, 3, [1, 12, 5])
