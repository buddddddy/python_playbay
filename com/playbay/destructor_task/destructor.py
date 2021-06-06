
class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surename = s
        self.qual = q

    def person_info(self):
        return f' Name: {self.name}, Surename: {self.surename}, qualification: {self.qual}'

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surename}')


p1 = Person('Юрий', 'Томилин', 3)
p2 = Person('Бобылев', 'Александр', 1)
p3 = Person('Каковкин', 'Алексей', 2)

