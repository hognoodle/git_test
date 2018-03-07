def objtest(obj1, obj2):

    if obj1 is obj2:
        print("Objects are the same")
    else:
        print("Objects are not the same")

class Shape():
    def __init__(self, shape):
        self.shape = shape


myshape_1 = Shape("triangle")
#myshape_2 = Shape("blob")
myshape_2 = myshape_1
#myshape_2 = Shape("triangle")

objtest(myshape_1, myshape_2)