
class Food:

    def __init__(self, cal=0, prot=0, fat=0, carb=0):
        self.__macros = {
            'cal': cal,
            'prot': prot,
            'fat': fat,
            'carb': carb
        }

    def set_macros(self, cal, prot, fat, carb):

        self.__macros = {
            'cal': cal,
            'prot': prot,
            'fat': fat,
            'carb': carb
        }

    def edit_macro(self, macro, new_value):
        self.__macros[macro] = new_value

    def get_attr(self, param):
        return self.__macros[param]

    def __str__(self):
        return f'' \
               f'Cal: {self.__macros["cal"]}' \
               f' Proteins: {self.__macros["prot"]}' \
               f' Fats: {self.__macros["fat"]}' \
               f' Carbs: {self.__macros["carb"]}'

    def __add__(self, other):
        obj = Food()
        obj.set_macros(
            self.__macros["cal"] + other.__macros["cal"],
            self.__macros["prot"] + other.__macros["prot"],
            self.__macros["fat"] + other.__macros["fat"],
            self.__macros["carb"] + other.__macros["carb"])
        return obj

    def __setattr__(self, key, value):
        if key != '_Food__macros':
            raise AttributeError('Не делай этого, Мага!')
        else:
            self.__dict__[key] = value


class Porridge(Food):
    pass


class Meat(Food):
    pass


buckwheat = Food()
turkey = Food()
spinach = Food()

buckwheat.set_macros(330, 12.6, 3.3, 64)
turkey.set_macros(189, 29, 7, 0)
spinach.set_macros(23, 2.9, 0, 3.6)

rec1 = buckwheat + turkey
rec2 = rec1 + spinach

turkey.edit_macro('fat', 100)

rec3 = turkey + spinach

print(rec1)
print(rec2)
print(rec3)

# проверка:

# buckwheat.cal = 1 # попытка присваивания объекту класса нового атрибута - ok
# buckwheat.__macros['fat'] = 1000 # попытка изменения атрибута извне класса - ok, но отрабатывает не "мой" AttrErr
# print(rec1.get_attr('fat')) # тест доступа к атрибутам через метод - ок
# rec1.edit_macro('fat', 777) # тест изменения атрибута через метод - ок
'''
Не нравится, что параметры не обновляются "онлайн": после вызова turkey.edit_macro('fat', 100) значения по ключу 'fat'
должны обновляться, а они остаются теми же, какими были на момент создания объекта.
С другой стороны, такие изменения не должны производиться на постоянной основе: для, например, мяса разной жирности
можно создать разные объекты. Скорее всего, изменение кбжу может иметь место при обновлении базы в целях уточнения ну-
триентов. То есть, необходимости вызывать эти методы повторно возникать не должно.
'''