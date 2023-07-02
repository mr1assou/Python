from math import pi
class Shape:
    def __init__(self, pType, pArea):
        self.type = pType
        self.area = pArea
    def __str__(self) :
        return f'{self.type} of area {self.area:4.2f} units square'
    def __add__(self,other):
        new_area = self.area + other.area
        return Shape('New shape',new_area)
    def __radd__(self, other):
        return self.__add__(other)
class Square(Shape):
    def __init__(self, pLength):
        super().__init__('Square', 0)
        self.length = pLength   
        self.area = self.length*self.length
class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__('Triangle',0)
        self.base=base
        self.height=height
        self.area=0.5*base*height
class Cercle(Shape):
    def __init__(self,radius):
        super().__init__('cercle',0)
        self.radius=radius
        self.area=pi*self.radius**2