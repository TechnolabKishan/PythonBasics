# Poly = many morphe = Form 
# inheritance = an object could be treated of the same type as parent class
# 'duck typing' = object must have necessary attributes/ ethod
from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius): # many form of faces like pizza
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('broccoli', 15) ]

for shape in shapes:
    print(shape.area())

