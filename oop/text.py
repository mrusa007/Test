class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def __init__(self, length, width, name="Rectangle"):
        Shape.__init__(self, name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, "Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side, "Square")
shapes = [Rectangle(5, 3), Circle(2), Square(4)]

for s in shapes:
    print(f"{s.name} area: {s.area():.2f}")