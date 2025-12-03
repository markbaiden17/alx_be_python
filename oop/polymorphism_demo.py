import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        NotImplementedError

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)