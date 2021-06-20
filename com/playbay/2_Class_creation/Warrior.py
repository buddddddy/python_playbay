class Warrior:

    hp = 100
    impact = -20
    name = None

    def set_name(self, name):
        self.name = name

    def attack(self, enemy):
        enemy.hp -= 20
        print(self.name, 'hits', enemy.name)
        print('%s: %d hp' % (enemy.name, enemy.hp))

    def is_live(self):
        return self.hp > 0




