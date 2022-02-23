from turtle import circle


class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        Area = 3.1414 * self.r ** 2
        return Area


C1 = Circle(17)
C2 = Circle(2)
print(C1.Area())
print(C2.Area())