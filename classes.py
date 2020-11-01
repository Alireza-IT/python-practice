# class :blueprint for cerating new object
# Object : instance of a class
# class : Human
# objects: john, alireza , jack

class Point:
    default_color = "red"  # class level attribute like each human has 2 eyes and shares between all object adn all instances

    def __init__(self, x, y):  # magic method which is contructor and executed when create a new object and x and y is optional
        # when creating point object the object is creating in memory and self is pointing into current point obj and this has lot of attribute and built in datas
        self.x = x  # most of time we use instance atrributes but we can build class level attribute to share between obj
        self.y = y
        
    def draw(self): #instance method and call from instance of class
        # refer to current obj and read the values of x and y and we can print them
        print(f"Point ({self.x} , {self.y})")
        print("draw")
# need some initial values that we need constructor
    @classmethod #it's decorader and extend behaivor of method or function
    def zero(cls): #reference to it's clas
        return cls(0 , 0 ) #exactly like Point (0,0) and it runs at runtime and pass the values


point = Point(1, 2)
point.default_color
point.z = 10 #create new attribute and it's instance attribute
print(type(point))
print(isinstance(point, Point)) 
# //checking if the point is instance point class or not.
print(point.x)
point.draw()

another = Point(3, 4)
another.draw()
point2 = Point.zero() #it's class method that when initialize use this values