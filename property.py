class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        try:
            return f'{self._width:.1f} cm'
        except AttributeError:
            return 'width is deleted'

    @property
    def height(self):
        try:
            return f'{self._height:.1f} cm'
        except AttributeError:
            return 'height is deleted'


    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('it should be higher than 0')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('it should be higher than 0')

    @width.deleter
    def width(self):
        del self._width

    @height.deleter
    def height(self):
        del self._height


rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 7

del rectangle.width
del rectangle.height

print(rectangle.width)  # Nu: 'width is deleted'
print(rectangle.height)  # Nu: 'height is deleted'
