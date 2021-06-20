from random import randrange


number_of_players = int(input('количество игроков:'))

number_of_teams = int(input('Количество команд:'))

free_ids = set(range(number_of_players))

team_count = 0


class Unit:

    def __init__(self):
        global team_count
        global free_ids
        self.id_ = free_ids.pop()
        if isinstance(self, Hero):
            self.followers = []
            self.team = team_count + 1
            team_count += 1
        else:
            rand_team = randrange(1, number_of_teams + 1)
            self.team = rand_team
            list_of_heroes[rand_team - 1].followers.append(self)


class Soldier(Unit):
    def follow_hero(self, follow_this_hero):
        print(f'Солдат № {self.id_} следует за героем № {follow_this_hero.id_}')


class Hero(Unit):
    lvl = 0

    def lvl_up(self):
        self.lvl += 1
        print(f'Уровень героя команды № {self.team} повысился с {self.lvl - 1} до {self.lvl}')


list_of_heroes = [Hero() for i in range(number_of_teams)]

for _ in range(number_of_players - team_count):
    _ = Soldier()

for obj in list_of_heroes:
    print(f'У команды №{obj.team} {len(obj.followers)} солдат')

sorted(list_of_heroes, key=lambda p: len(p.followers))[-1].lvl_up()

list_of_heroes[0].followers[randrange(len(list_of_heroes[0].followers))].follow_hero(list_of_heroes[0])


'''
id_gen должна была генерировать id от 0 до кол-ва объектов класса Unit c целью не хранить длинный список из всех
id в памяти, но в итоге так оно и получилось. Плюс при большом кол-ве объектов (уже от 800 на практике) рекурсия
 может достигнуть максимальной глубины из-за того, что кол-во вариантов id равно кол-ву объектов. Поэтому диапа-
 зон был расширен в 10 раз. Лучше бы я сначала сгенерировал список из всех id, а затем pop-ал бы оттуда рандом-
 чойсом: занимает памяти не больше, а в конце бы список вообще стал пуст. - так и сделал
 Сейчас принадлежность команде определяется в конструкторе класса Unit: для класса Hero номер команды равен по-
 рядковому номеру объекта, для Soldier - выбирается случайным образом из диапазона [1, кол-во команд + 1). 
 Проблема в том, как сформировать списки солдат для команд и вывести их на экран, а также измерить длину списков
 для того, чтоб какому-то герою увеличить уровень. - решена путём хранения всех объектов класса Hero в списке, 
 что позволяет обращаться к любому объекту по индексу списка.
Протестировано с кол-вом героев 10^6 - полёт нормальный. Защиту от дурака на кол-во команд и кол-во игроков де-
лать не буду.
Судя по распределению солдат по командам, randrange использует нормальное распределение
'''