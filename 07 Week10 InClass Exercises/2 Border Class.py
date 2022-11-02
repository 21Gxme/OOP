from vector import Vector

class Border:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"Border(corner={self.corner},"
                f" width={self.width}, height={self.height})")

    # insert your new method(s) here (don't forget the indentation)
    @property
    def corner(self):
        return self.__corner

    @corner.setter
    def corner(self, value):
        if not isinstance(value, Vector):
            raise TypeError("corner must be a Vector object")
        else:
            self.__corner = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be a number")
        elif value < 1:
            raise ValueError("width must be greater than zero")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be a number")
        elif value < 1:
            raise ValueError("height must be greater than zero")
        else:
            self.__height = value

