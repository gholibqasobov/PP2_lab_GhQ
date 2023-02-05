from math import sqrt


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, x, y):
        d = sqrt(pow((self.x - x), 2) + pow((self.y - y), 2))
        print(d)


figure1 = Point(4, 5)

figure1.move(4, 5)
figure1.show()
figure1.dist(2, 3)
