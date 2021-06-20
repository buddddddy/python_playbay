import sys
import room_with_doc
# import sys

sys.stdin = open("/python_playbay/com/playbay/7_composition/composition_inp.txt")


while True:
    room_w, room_l, room_h = (int(i) for i in input('w, l, h of room \n').split())
    r = room_with_doc.Room(room_w, room_l, room_h)

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
