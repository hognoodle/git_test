class Horse():
    def __init__(self, color, gender, rider):
        self.color = color
        self.gender = gender
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

bob = Rider("Bob Johnson")
pally = Horse("white", "f", bob)
print(pally.color)
print(pally.rider.name)
