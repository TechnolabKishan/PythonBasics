# super() = function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality or the inherited methods

class shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled 

    def describe(self):
        print(f'it is {self.color} and {"filled" if self.is_filled else "not filled"}')  
        

class Circle(shapes):
    def __init__(self,color , is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f'it is circle with an area of {3.14 * self.radius * self.radius}cm^2')
        super().describe()

class Square(shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f'het is een kubs arena van {self.width * self.width }cm^2')
        super().describe()

class Triangle(shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f'het is een driekhoek arena van {1/2 * self.width * self.height}')


circle = Circle(color='red', is_filled=True, radius=5)
square = Square(color='blue', is_filled=False, width=6)
triangle = Triangle(color='blue', is_filled=True, width=5, height=7)
circle.describe()
triangle.describe()
square.describe()

