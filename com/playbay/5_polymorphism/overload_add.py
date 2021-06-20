
class Food:

    def __init__(self, cal, prot, fat, carb):
        self.cal = cal
        self.prot = prot
        self.fat = fat
        self.carb = carb

    def __str__(self):
        return f'Cal: {self.cal} Proteins: {self.prot} Fats: {self.fat} Carbs: {self.carb}'

    def __add__(self, other):
        return Food(self.cal + other.cal, self.prot + other.prot, self.fat + other.fat, self.carb + other.carb)


class Porridge(Food):
    pass


class Meat(Food):
    pass


buckwheat = Porridge(330, 12.6, 3.3, 64)

turkey = Meat(189, 29, 7, 0)

print(buckwheat + turkey)
