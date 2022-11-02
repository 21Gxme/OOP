class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_x_axis(self):
        return self.y == 0

    def is_on_y_axis(self):
        return self.x == 0

    def translate(self, distX, distY):
        self.x += distX
        self.y += distY

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

class PointApp:
    p1 = Point(20, 100)
    p2 = Point(-40, 50)
    print(p1.is_on_x_axis())
    print(p2.is_on_y_axis())
    p1.translate(-60, -50)
    print(p1 == p2)
    print(p1)
    print(p2)