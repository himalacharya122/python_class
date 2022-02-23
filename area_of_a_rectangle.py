class Rectangle:
    def __init__(self, Length, Breadth,):
        self.Length = Length
        self.Breadth = Breadth
    
    def Area(self):
        Area = self.Length * self.Breadth
        return Area
        
r1 = Rectangle(10, 5)
r2 = Rectangle(19.5, 89)
print(r1.Area())
print(r2.Area())