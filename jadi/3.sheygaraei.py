class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        print("name is %s" % self.name)

    def get_age(self):
        print("age is %s" % self.age)

    def get_info(self):
        print("name is %s and age is %i" % (self.name, self.age))

    def birthdate(self):
        self.age = self.age + 1
        print("happy birthday %s " % self.name)

    def return_count(self):
        return(Person.count)


alireza = Person('alireza', 27)

alireza.get_name()
alireza.birthdate()
alireza.get_info()


jadi = Person("jadi", 12)

jadi.get_age()
jadi.count


print("finally %s ", jadi.return_count())
