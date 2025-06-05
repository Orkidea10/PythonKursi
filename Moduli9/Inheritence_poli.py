import math
from curses.textpad import rectangle


class Shape:
    def area(self):
        pass



class circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius **2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5 * self.base * self.height




rrethi= circle(6)
drejtkendeshi= Rectangle(6,4)
trekendeshi= Triangle(4,6)
