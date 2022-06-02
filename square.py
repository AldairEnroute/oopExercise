from tokenize import Double
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, color:str, filled:bool, side:Double):
        super().__init__(color, filled, width=side, length=side)
    def getSide(self) -> Double:
        return self._width
    def setSide(self, side:Double) -> Double:
        self.setWidth(side)
        self.setLength(side)
    def setWidth(self, side:Double) -> Double:
        self._width = self._length = side
    def setLength(self, side:Double) -> Double:
        self._width = self._length = side
    def __str__(self) -> str:
        return f'Square[{super(Square, self).__str__()}]'
cuadradin = Square('Red',True,4)
print('Area: ',(cuadradin.getArea()))
print('Perimeter: ',(cuadradin.getPerimeter()))
print(cuadradin)
