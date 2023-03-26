class Container:
    ''' This is a meta class that's supposed to NOT have an initializer.
        It's only to be extended upon.
    '''

    def __init__(self):
        pass


class Box(Container):
    ''' A cuboid box, having width, depth, and height.
        When initializing the dimensions should be in cm.
        The dimcost is the sum of all three sides.
    '''

    def __init__(self, width, depth, height):
        self.__width = width
        self.__depth = depth
        self.__heigth = height
        self.update_dims()

    def update_dims(self):
        self.__dim_cost = self.__width + self.__depth + self.__height
        self.__volume = self.__width * self.__depth * self.__height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width
        self.update_dims()

    def get_depth(self):
        return self.__depth

    def set_depth(self, depth):
        self.__depth = depth
        self.update_dims()

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height
        self.update_dims()

    def get_dim_cost(self):
        return self.__dim_cost

    def get_volume(self):
        return self.__volume

    class Cylinder(Container):
        pass