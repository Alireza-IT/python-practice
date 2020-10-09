# class :blueprint for cerating new object
# Object : instance of a class
# class : Human
# objects: john, alireza , jack

class Point:
    default_color = "red"  # class level attribute

    def __init__(self, x, y):  # magic method which is contructor and executed when create a new object and x and y is optional
        # self is pointing into current point obj and this has lot of attribute and built in datas
        self.x = x  # most of time we use instance atrributes but we can build class level attribute to share between obj
        self.y = y

    def draw(self):
        # refer to current obj and read the values of x and y adn we can print them
        print(f"Point ({self.x} , {self.y})")
        print("draw")
# need some initial values that we need constructor


point = Point(1, 2)
point.default_color
point.z = 10
print(type(point))
print(isinstance(point, Point))
print(point.x)
point.draw()

another = Point(3, 4)
another.draw()
