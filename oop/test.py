class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.name = "Rectangle"
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side):
        self.name = "Square"
        self.length = side
        self.width = side
shapes = [Rectangle(5, 3), Circle(2), Square(4)]

for s in shapes:
    print(s.name, "area:", round(s.area(), 2))