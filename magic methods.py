class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # use this instead of using str(point) in our program
        return f"({self.x},{self.y}"

    def draw(self):
        print(f"Point ({self.x},{self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # return true if equal

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
point.__str__  # return the classname of this object by using the memory address
print(point)

other = Point(1, 2)

# return false because it compares the reference address of two obj instead of the their values
print(point == other)  # use line 13
# so instead we have to use magic method when we compare two obj
print(point > other)  # use line 15
