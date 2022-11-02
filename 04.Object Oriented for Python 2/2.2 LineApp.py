class Point:
    def __init__(self,x,y):
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

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)
        self.slope = (y2 - y1) / (x2 - x1)
        self.yintercept = y1 - self.slope * x1

    def contains(self, x, y):
        return min(self.start_point.get_x(), self.end_point.get_x()) <= x <= max(self.start_point.get_x(), self.end_point.get_x()) and min(self.start_point.get_y(), self.end_point.get_y()) <= y <= max(self.start_point.get_y(), self.end_point.get_y())

    def get_distance(self):
        return ((self.start_point.get_x() - self.end_point.get_x()) ** 2 + (self.start_point.get_y() - self.end_point.get_y()) ** 2) ** .5

    def get_x1(self):
        return self.start_point.get_x()

    def get_y1(self):
        return self.start_point.get_y()

    def get_x2(self):
        return self.end_point.get_x()

    def get_y2(self):
        return self.end_point.get_y()

    def get_y(self, x):
        if self.contains(x, self.slope * x + self.yintercept):
            return self.slope * x + self.yintercept
        return -999.999

class LineApp:

    def __init__(self):
        line = Line(int(input("Enter x1 : ")), int(input("Enter x2 : ")), int(input("Enter y1 : ")), int(input("Enter y2 : ")))
        print(f"value of x1 on this line is {line.x1:.3f}")
        print(f"value of x2 on this line is {line.x2:.3f}")
        print(f"value of y1 on this line is {line.y1:.3f}")
        print(f"value of y2 on this line is {line.y2:.3f}")
        print("==========")
        print("Check x and y are on this line ?")
        x = int(input("Enter x : "))
        y = int(input("Enter y : "))
        if line.is_on_line(x, y):
            print(f"x = {x:.3f} and y = {y:.3f} are on this line")
        else:
            print(f"x = {x:.3f} and y = {y:.3f} are not on this line")
        print(f"Distance between startPoint and endPoint is {line.distance():.3f}")
        print("==========")
        print("Find value of y that gives( x , y ) on this line ")
        x = int(input("Enter x : "))
        print(f"value of y is {line.find_y(x):.3f}")
        print(f"( x , y ) = ( {x:.3f} , {line.find_y(x):.3f} ) on this line")

c= LineApp()