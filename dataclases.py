# only for classes that holds only data
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
# p2.x = 10  # got error
p2 = Point(x=1, y=2)

print(p1 == p2)
# there is no need to implemet the magic method
# helps to write less code
# it's immutable
