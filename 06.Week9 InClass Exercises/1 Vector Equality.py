import math

class Vector:
    """ Define a vector in 2D space

    # all methods from previous exercises already defined here, but hidden

    # insert your new method(s) here (don't forget the indentation)
    >>> v1 = Vector(3, 4)
    >>> v2 = Vector(3, 4)
    >>> v3 = Vector(3, 6)
    >>> v4 = Vector(5, 4)
    >>> v1 == v2
    True
    >>> v1 == v3
    False
    >>> v1 == v4
    False
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)



