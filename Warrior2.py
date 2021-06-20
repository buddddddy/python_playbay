from random import randint


class Warrior:

    hp = 100

    def set_name(self, name):
        self.name = name

    def kick(self, attacked):
        attacked.hp -= 20
        print(f'{self.name} attacked {attacked.name}. {attacked.name} has {attacked.hp} hp')


Unit1 = Warrior()
Unit2 = Warrior()

Unit1.set_name('Unit1')
Unit2.set_name('Unit2')

while Unit1.hp > 0 and Unit2.hp > 0:
    if randint(0, 100) >= 50:
        Unit1.kick(Unit2)
    else:
        Unit2.kick(Unit1)

print('%s win with hp = %d' % ((Unit1.name, Unit1.hp) if Unit2.hp == 0 else (Unit2.name, Unit2.hp)))
