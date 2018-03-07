class Triangle():

    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 0.5 * self.base * self.height

myTriangle = Triangle(12, 4)
print("Triangle area is " + str(myTriangle.area()))