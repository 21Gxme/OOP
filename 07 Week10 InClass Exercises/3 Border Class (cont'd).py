from vector import Vector

class Border:
    """Define a border in 2D space with the lower-left corner, width, and height."""

    # all methods from previous exercises already defined here, but hidden

    # insert your new method(s) here (don't forget the indentation)
    @property
    def left(self):
        return self.corner.x

    @property
    def right(self):
        return self.corner.x + self.width

    @property
    def bottom(self):
        return self.corner.y

    @property
    def top(self):
        return self.corner.y + self.height

    @property
    def sides(self):
        return self.left, self.right, self.bottom, self.top