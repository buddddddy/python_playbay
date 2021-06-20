from random import randint


class Unit:
    def __init__(self, n, t):
        self.number = n
        self.team = t


class Soldier(Unit):
    def follow_hero(self, pursued):
        print(f'Солдат №{self.number} следует за героем №{pursued.number}')


class Hero(Unit):
    def __init__(self, n, t, lvl):
        Unit.__init__(self, n, t)
        self.level = lvl

    def level_up(self):
        self.level += 1


list_of_heroes = []                  # Создание пустого списка объектов класса Hero
list_of_soldiers = []                # Создание пустого списка списков объектов класса Soldier

for i in range(int(input(
        'Количество героев: '))):    # Создание списка заданного кол-ва героев и пустых списков для списков объектов класса Soldier
    h = Hero(i, i, 0)                # Создание объекта класса Hero
    list_of_heroes.append(h)         # Добавление созданного объекта в список
    list_of_soldiers.append([] * i)  # Создание вложенных списков объектов класса Soldier

for j in range(100):                                # Создание объектов класса Soldier и их сортировка по спискам команд
    s = Soldier(n=j + len(list_of_heroes),
                t=randint(0, len(list_of_heroes)))  # нумерация и присваивание одной из команд
    list_of_soldiers[s.team - 1].append(s)          # добавление во вложенный список этой команды

score_list = []       # Создание пустого списка, чтобы из него получить значение длин списков солдат (и максимума длины)

for z in range(len(list_of_heroes)):                # Заполнение созданного ранее списка значениями длин списков
    score_list.append(len(list_of_soldiers[z]))     # объектов класса Soldier

for k in range(len(list_of_heroes)):                    # Вывод длин списков объектов класса Soldier каждой команды и
    print(f'У команды № {k} {len(list_of_soldiers[k])} солдат')  # сравнение со значением самого длинного списка
    if len(list_of_soldiers[k]) == max(score_list):     # Если обрабатываемый список самый длинный, объектам типа Hero
        list_of_heroes[k].level_up()                    # этого списка повышаем уровень

for x in range(len(list_of_heroes)):                    # Вывод уровней всех команд
    print(f'У команды {x} {list_of_heroes[x].level} уровень')

p = randint(0, len(list_of_soldiers[0]))                # Параметр для последнего выражения. Выбирает рандомного солдата
                                                        # из команды №1
list_of_soldiers[0][p].follow_hero(list_of_heroes[0])   # Рандомный солдат команды №1 следует за героем №1, выводятся
                                                        # их идентификационные номера
