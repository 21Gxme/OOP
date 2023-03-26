import math

class Container:
    ''' This is a meta class that's supposed to NOT have an initializer.
        It's only to be extended upon.
    '''
    def __init__(self):
        pass

class Banana(Container):
    ''' The Banana box.
        Define the volume and dim_cost using length and radius at the widest part.
    '''
    def __init__(self, length, radius):
        if length < 4 * radius:
            raise ValueError
        self.__length = length
        self.__radius = radius

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length < 4 * self.__radius:
            raise ValueError
        self.__length = length

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError
        self.__radius = radius

    @property
    def dim_cost(self):
        return float(self.__length + (2 * self.__radius))

    @property
    def volume(self):
        return float((4/3)*math.pi*self.__length*self.__radius**2)
