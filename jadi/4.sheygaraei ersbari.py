class Computer:

    count = 0  # moshtarke va age taghiri az taraf ye objecti ru in beshe bara hame avaz mishe

    def __init__(self, ram, hard, cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu

    def __del__(self):  # harmoqe ino delte kardi in etefagha biofte
        Computer.count -= 1


class Loptop(Computer):
    # //inherit form computer
    def value(self):
        return self.ram + self.hard + self.cpu + self.size

    pass


pc1 = Computer(12, 2, 4)
pc2 = Computer(8, 4, 4)

print(pc1.value())
print(pc2.value())


loptop1 = Loptop(16, 2, 4)
loptop1.size = 13
print(loptop1.value())
