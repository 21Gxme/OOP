import math


class Circle:
    def __init__(self, x=0, y=0, radius=0):
        self.x = x
        self.y = y
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * pow(self.radius, 2)

    def get_center_x(self):
        return self.x

    def get_center_y(self):
        return self.y

    def get_radius(self):
        return self.radius

    def set_center_x(self, x):
        self.x = x

    def set_center_y(self,y):
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}), Radius: {self.radius:.1f}"
