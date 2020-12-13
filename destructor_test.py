
class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualification = q

    def get_info(self):
        return self.surname, self.name, self.qualification

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}.')


Alexander = Person("Александр", 'Бобылев', 1)
Aleksey = Person('Алексей', 'Каковкин', 3)
Yuri = Person('Юрий', 'Томилин', 2)

print(Person.get_info(Alexander))
print(Person.get_info(Aleksey))
print(Person.get_info(Yuri))

input()


