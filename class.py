

class Point:

    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # its decorader that change behave of class
    def zero(cls):  # reference to class itself  for factory method
        return cls(0, 0)

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def draw(self):

        print(f"Point ({self.x} , {self.y})")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other = Point(10, 2)
point.z = 10
print(isinstance(point, int))
point = Point.zero()  # refer to factory method
point.draw()
