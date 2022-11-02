class Radio:

    def __init__(self):
        self.mode = "FM"
        self.frequency = 87.5

    def set_mode(self, mode):
        self.mode = mode
        if mode == "FM":
            self.frequency = 87.5
        elif mode == "AM":
            self.frequency = 150

    def set_frequency(self, frequency):
        if self.mode == "FM" and 87.5 <= frequency <= 108:
            self.frequency = frequency
        elif self.mode == "AM" and 150 <= frequency <= 280:
            self.frequency = frequency

    def adjust_frequency(self, frequency):
        if self.mode == "FM" and 87.5 <= self.frequency + frequency <= 108:
            self.frequency = self.frequency + frequency
            return True
        elif self.mode == "AM" and 150 <= self.frequency + frequency <= 280:
            self.frequency = self.frequency + frequency
            return True
        else:
            return False

    def get_mode(self):
        return self.mode

    def get_frequency(self):
        return self.frequency

    def __str__(self):
        return f"{self.mode} Radio: {self.frequency:.1f} {'MHz' if self.mode == 'FM' else 'kHz'}"