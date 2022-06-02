import math
from tokenize import Double
from shape import Shape

class Triangle(Shape):
    def __init__(self, color:str, filled:bool = True, sideLength:Double = 1.0):
        super().__init__(color, filled)
        self._sideLength = sideLength
    def getSideLength(self) -> Double:
        return self._sideLength
    def setSideLength(self, _sideLength:Double) -> Double:
        self._sideLength = _sideLength
    def getArea(self) -> Double:
        area = ((math.sqrt(3))*((self._sideLength ** 2)))/4
        return area
    def getPerimeter(self) -> Double:
        perimeter = self._sideLength + self._sideLength + self._sideLength
        return perimeter
    def __str__(self) -> str:
        return f'Equilateral Triangle[{super(Triangle, self).__str__()}, side length = {self._sideLength}]'

triangulo = Triangle('Red')
triangulo.setSideLength(11)
print('Area: ',(triangulo.getArea()))
print('Perimeter: ',(triangulo.getPerimeter()))
print(triangulo)