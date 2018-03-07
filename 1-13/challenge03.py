class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass


shape = Shape()
print(shape.what_am_i())

square = Square()
print(square.what_am_i())

rectangle= Rectangle()
print(rectangle.what_am_i())

