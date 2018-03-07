class Square():

    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

my_square = Square(11)
print(my_square)