import sys

sys.stdin = open('composition_inp.txt', 'r')


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


room_w, room_l, room_h = (int(i) for i in input('w, l, h of room \n').split())
r = Room(room_w, room_l, room_h)

roll_w, roll_h = map(float, input('w, h of roll \n').split())
windor_count = int(input('How much windows and doors add? \n'))

if windor_count == 0:
    print('Without windows without doors полна жопа огурцов \n')
else:
    for n in range(windor_count):
        wd_w, wd_h = map(float, input('Input width and height of window or door \n').split())
        r.add_wd(wd_w, wd_h)

print(f'Surface to be wallpapered: {r.get_sq_to_wallpaper()}')
print(f'Required amount of rolls is {r.how_much_such_roll(roll_w, roll_h)}')
