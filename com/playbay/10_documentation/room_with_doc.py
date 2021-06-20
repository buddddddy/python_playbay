'''Module include two classes: 1)WinDoor to create an instance of door or window,\n2)Room with its constructor and methods'''
class WinDoor:
    '''Include constructor only which takes two args: width and length of an window or door instance to instantiate .square arg\n
    for objects of this class'''
    def __init__(self, x, y):
        self.square = x * y


class Room:
    '''Constructor takes width, length and height of an room and append it to corresponding args of objects of this class.\n 
    Constructor instantiate .wd arg to store instances of WinDoor class'''
    def __init__(self, width, length, height):
        self.width = width
        self.height = height
        self.length = length
        self.wd = []


    def how_much_such_roll(self, w, h):
        '''Method takes width and height of roll and return amount of such rolls to wallpaer given room'''
        room_square = 2 * self.height * (self.width + self.length) - sum(i.square for i in self. wd)
        roll_square = w * h
        return room_square // roll_square if room_square % roll_square == 0 else room_square // roll_square + 1

    def get_full_square(self):
        '''return raw square of given room(without doors and windows square'''
        return 2 * self.height * (self.width + self.length)

    def get_sq_to_wallpaper(self):
        '''return square to be wallpapered of given room'''
        return 2 * self.height * (self.width + self.length) - sum(i.square for i in self.wd)

    def add_wd(self, w, h):
        '''method to append instance of window or door to .wd arg of given Room object'''
        self.wd.append(WinDoor(w,h))

