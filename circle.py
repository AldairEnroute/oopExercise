import math
from tokenize import Double
from shape import Shape

class Circle(Shape):
    def __init__(self, color:str, filled:bool, radius:Double = 1.0):
        super().__init__(color, filled)
        self._radius = radius
    def getRadius(self):
        return self._radius
    def setRadius(self, x):
        self._radius = x
    def getArea(self, radius) -> Double:
        area = math.pi * (radius * radius)
        return area
    def getPerimeter(self, radius) -> Double:
        perimeter = (2 * math.pi) * radius
        return perimeter
    def __str__(self) -> str:
        return f'Circle[{super(Circle, self).__str__()}, radius = {self._radius}]'

circulo = Circle('Red',True)
print('Perimeter: ',circulo.getPerimeter(8))
print('Area: ',circulo.getArea(4))
print(circulo)