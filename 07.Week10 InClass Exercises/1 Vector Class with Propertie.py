import math
import copy

class Vector:
    """ Define a vector in 2D space """

    def __init__(self, x=0, y=0):
        # assign __x and __y via their properties for input validation
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        else:
            self.__y = value

    def __str__(self):
        return f"Vector(x={self.x}, y={self.y})"
