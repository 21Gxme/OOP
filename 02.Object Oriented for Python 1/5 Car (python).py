class Car:
    def __init__(self, gas=0, burning_rate=0):
        self.gas = gas
        self.burning_rate = burning_rate

    def drive(self, distance):
        self.gas -= distance / self.burning_rate
        return self.gas

    def fill_gas(self, new_gas):
        self.gas += new_gas
        return self.gas

    def get_gas(self):
        return self.gas

    def set_gas(self, gas):
        self.gas = gas

    def get_burning_rate(self):
        return self.burning_rate

    def set_burning_rate(self, new_burning_rate):
        self.burning_rate = new_burning_rate

    def __str__(self):
        return "Gas: " + str(self.gas) + ", Burning rate: " + str(self.burning_rate)