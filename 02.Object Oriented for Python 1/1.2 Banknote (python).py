class Banknote:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return f'{self.value} Baht Banknote'

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


b = Banknote(30)
print(b)