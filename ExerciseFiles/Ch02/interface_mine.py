# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod
from math import pi

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * self.radius * self.radius

    def toJSON(self):
        return f"{{\" Circle\" : {str(self.calcArea())} }}" 


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
