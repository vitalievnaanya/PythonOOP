class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_num, guest_count):
        possible_rooms = [r for r in self.rooms if r.number == room_num]
        room = possible_rooms[0]

        if room.take_room(guest_count):
            return

        self.guests += guest_count

    def free_room(self, room_num):
        possible_rooms = [r for r in self.rooms if r.number == room_num]
        room = possible_rooms[0]

        if room.free_room():
            return

        self.guests -= room.guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        return f'Hotel {self.name} has {self.guests} total guests \n' \
               f'Free rooms: {", ".join(free_rooms)} \n' \
               f'Taken rooms: {", ".join(taken_rooms)}'
