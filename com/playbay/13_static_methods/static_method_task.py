
from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, diametr, high):
        self.__dict__['dia'] = diametr
        self.__dict__['h'] = high
        self.__dict__['area'] = self.make_area(diametr, high)

    def __setattr__(self, key, value):
        if key == 'dia':
            self.__dict__[key] = value
            self.__dict__['area'] = self.make_area(self.dia, self.h)
        elif key == 'h':
            self.__dict__[key] = value
            self.__dict__['area'] = self.make_area(self.dia, self.h)
        elif key == 'area':
            print("Поле недоступно для изменения извне класса")


a = Cylinder(1, 2)

print(a.area)

a.dia = 4.5
a.h = 3.3

print(a.area)

a.area = 100