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
