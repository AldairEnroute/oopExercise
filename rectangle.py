from tokenize import Double
from shape import Shape

class Rectangle(Shape):
    def __init__(self, color:str, filled:bool, width:Double = 1.0, length:Double = 1.0):
        super().__init__(color, filled)
        self._width = width
        self._length = length

    def getWidth(self):
        return self._width
    def setWidth(self,width:Double):
        self._width = width
    def getLength(self):
        return self._width
    def setLength(self, length:Double):
        self._length = length
    def getArea(self) -> Double:
        area = self._length * self._width
        return area
    def getPerimeter(self) -> Double:
        perimeter = (self._length * 2) + (self._width * 2)
        return perimeter
    def __str__(self) -> str:
        return f'Rectangle[{super(Rectangle, self).__str__()}, width = {self._width}, length = {self._length}]'

rectangular = Rectangle('Red',True,8,5)
print('Area:',(rectangular.getArea()))
print('Perimeter: ',(rectangular.getPerimeter()))
print(rectangular)