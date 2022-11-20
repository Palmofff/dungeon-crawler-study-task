class Weapon:
    def __init__(self, name, lvl, attack, damage):
        self.name = name
        self.lvl = lvl
        self.attack = attack
        self.damage = damage 
battleaxe = Weapon("battleaxe", 1, [1, 20, 1], [1, 8, 2]) # where [1, 20, 1] is 1d20+1
scimitar = Weapon("scimitar",1, [1, 20, 3], [1, 6, 1])
sickle = Weapon("sickle", 1, [1, 20, 5], [1, 4, 1])
shortsword = Weapon("shortsword", 3, [1, 20, 3], [1, 6, 2])
maul = Weapon("maul", 3, [1, 20, 0], [2, 6, 1])
war_pick = Weapon("war pick", 3, [1, 20, 2], [1, 8, 0])
lance = Weapon("lance", 5, [1, 20, 2], [1, 12, 0])
rapier = Weapon("rapier", 5, [1, 20, 4], [1, 8, 2])
longsword = Weapon("longsword", 7, [1, 20, 5], [1, 8, 3])
greatsword = Weapon("greatsword", 7, [1, 20, 2], [2, 6, 3])
halebard = Weapon("halebard", 9, [1, 20, 5], [1, 10, 5])
greataxe = Weapon("greataxe", 9, [1, 20, 3], [1, 12, 5])