
class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualification = q

    def get_info(self):
        return self.surname, self.name, self.qualification

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}.')


alexander = Person("Александр", 'Бобылев', 1)
aleksey = Person('Алексей', 'Каковкин', 3)
yuri = Person('Юрий', 'Томилин', 2)

print(alexander.get_info())
print(aleksey.get_info())
print(yuri.get_info())

input()
