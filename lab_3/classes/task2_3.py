class Shape:
    length = 0

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length, 2)


figure1 = Shape()

figure2 = Square(3)

print(figure2.area())




# task 3

class Rectangle(Shape):
    width = 0

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width


figure3 = Rectangle(3, 4)

print(figure3.area())
