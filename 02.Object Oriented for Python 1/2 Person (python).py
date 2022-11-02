class Person:

    def __init__(self, ID="", name="", lastname="", gender="", age=0):
        self.ID = ID
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.ID}, {self.name} {self.lastname}, {self.gender}, {self.age}'

    def set_id(self, ID):
        self.ID = ID

    def get_id(self):
        return self.ID

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_gender(self,gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age

