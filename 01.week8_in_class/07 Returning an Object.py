import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def subtract(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def multiply(self, s):
        return Vector(self.x * s, self.y * s)


u = Vector(2, 5)
v = Vector(3, 8)
z = v.add(u.multiply(2))
print(u, v, z)