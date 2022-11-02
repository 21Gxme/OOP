import math

class Vector:
    """ Define a vector in 2D space """

    # __init__ already defined here, but hidden

    # insert your 'length' method here (don't forget the indentation)
    def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

    def length(self):
        return math.sqrt(self.x**2+self.y**2)