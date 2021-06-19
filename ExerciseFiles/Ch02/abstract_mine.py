# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod
from math import pi

class GraphicShape:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return  pi * self.radius * self.radius

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side



# If GraphicShape does not include an abstractmethod function decorator,
# an object of GraphicShape can be instantiated.
# Once a function has the abstractmethod decorator, an object instantiation
# throws an error.

# g = GraphicShape()

# Once there is a function with an abstractmethod decorator, on instantiation
# of the subclass throws an error, if the method has not been overriden.

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
