class Armor:
    def __init__(self, name, lvl, ac):
        self.name = name
        self.lvl = lvl
        self.ac = ac
leather = Armor("leather armor", 1, 12)
iron = Armor("iron armor", 3, 14)
adamantine = Armor("adamantine armor", 5, 16)
dragon = Armor("dragon scale armor", 7, 18)
demonic = Armor("demonic armor", 9, 20)