class Switch:
    def __init__(self, state):
        self.state = state

    def turn(self):
        if self.state == 'on':
            self.state = 'off'
        else:
            self.state = 'on'

    def clone(self):
        return Switch(self.state)

    def __str__(self):
        return f'switch({self.state}) is {self.state}'

class Light:
    def __init__(self, name, switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return self.switch

    def set_switch(self, new_switch):
        self.switch = new_switch

    def clone(self):
        return Light(self.name + '.copy', self.switch.clone())

    def __str__(self):
        return f'light({self.name}) with {self.switch}'



