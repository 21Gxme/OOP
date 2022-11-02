import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def dot(self,v):
        return (self.x * v.x)+(self.y * v.y)