from random import randint

class Warrior:

    hp = 100


    def set_name(self, name):
        self.name = name

    def reduce_hp(self, unit):
        unit.hp -= 20
        print(self.name, 'бьёт', unit.name)
        print('%s = %d здоровья' % (unit.name, unit.hp))

unit1 = Warrior()
unit2 = Warrior()

unit1.set_name('первый')
unit2.set_name('второй')

while unit1.hp > 0 and unit2.hp > 0:
    choose_attacker = randint(1, 2)

    if choose_attacker == 1:
        unit1.reduce_hp(unit2)
    else:
        unit2.reduce_hp(unit1)

if unit1.hp > unit2.hp:
    print('Первый победил с остатком здоровья', unit1.hp)
else:
    print('Второй победил с остатком здоровья', unit2.hp)