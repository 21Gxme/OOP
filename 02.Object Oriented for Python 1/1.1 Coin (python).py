class Coin:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return f'{self.value} Baht Coin'

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

c = Coin(5)
print(c)
