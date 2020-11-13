class Animal:  # inherite from object
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal)


def fly(self):
    print("fly")


print(issubclass(Mammal, object))

m = Mammal()
# m.eat()
# print(m.age)
print(m.age)
print(m.weight)
# print(isinstance(m, Mammal))
