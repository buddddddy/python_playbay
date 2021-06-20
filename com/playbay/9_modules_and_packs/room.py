
class WinDoor:
    def __init__(self, x, y):
       self.square = x * y


class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd = []

    def how_much_such_roll(self, w, h):
        room_square = 2 * self.height * (self.width + self.length) - sum(i.square for i in self.wd)
        roll_square = w * h
        return room_square // roll_square if room_square % roll_square == 0 else room_square // roll_square + 1

    def get_full_square(self):
        return 2 * self.height * (self.width + self.length)

    def get_sq_to_wallpaper(self):
        return 2 * self.height * (self.width + self.length) - sum(i.square for i in self.wd)

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))
