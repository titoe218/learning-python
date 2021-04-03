import math


class myCircle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(self.radius**2*math.pi, 2)

    def perimeter(self):
        return round((self.radius * 2 * math.pi), 2)


myCir = myCircle(int(input()))
print(myCir.area())
print(myCir.perimeter())
