class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length * 2 + self.width * 2

class Square():
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, change):
        self.length += change
        return self.length * 4



rectangle = Rectangle(4, 8)
print(rectangle.calculate_perimeter())

square = Square(6)
print(square.calculate_perimeter())
print(square.change_size(-1))