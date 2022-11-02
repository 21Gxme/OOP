class Location:
    def __init__(self, room='', floor=0):
        self.person = ''
        self.room = room
        self.floor = floor

    def __str__(self):
        if self.person == '':
            return f'{self.room} on floor {self.floor}. No one is in this room.'
        else:
            return f'{self.room} on floor {self.floor}. {self.person} is in this room.'

    def set_person(self, person):
        self.person = person

    def get_person(self):
        return self.person

    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room

    def set_floor(self, floor):
        self.floor = floor

    def get_floor(self):
        return self.floor