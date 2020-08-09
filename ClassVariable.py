class Circle:
    pi = 3.141592653589793238
    def __init__(self, radius):
        self.r = radius
    def calc_circum(self):
        return 2*self.r*Circle.pi
    def calc_area(self):
        return Circle.pi*self.r*self.r

C1 = Circle(5)
print(C1.calc_area())
print(C1.calc_circum())