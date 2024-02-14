

class Rectangle :
    def __init__(self, a,b ):
        self.a = a
        self.b = b

    def surface(self):
        return self.a*self.b


monrectangle = Rectangle (2,2)
s= monrectangle.surface()


