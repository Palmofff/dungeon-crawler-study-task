class Race:
    def __init__(self, name, attack_bonus, ac):
        self.name = name
        self.attack_bonus = attack_bonus
        self.ac = ac


human = Race("human", 1, 1)
dwarf = Race("dwarf", 0, 2)
elf = Race("elf", 3, -1)
orc = Race("orc", 2, 0)
