
class Person:
    #personal = []

    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qual = q
        #Person.personal.append(self)

    def person_info(self):
        return f' Name: {self.name}, Surname: {self.surname}, qualification: {self.qual}'

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}')
        del self


#p1 = Person('Юрий', 'Томилин', 3)
#p2 = Person('Александр', 'Бобылев', 1)
#p3 = Person('Алексей', 'Каковкин', 2)

#Person.personal.sort(key=lambda i: i.qual)

#while len(Person.personal) > 0:
    #del Person.personal[0]
    #print(Person.personal)

personal = [
    Person('Юрий', 'Томилин', 3),
    Person('Александр', 'Бобылев', 1),
    Person('Алексей', 'Каковкин', 2)
]

personal.sort(key=lambda p: p.qual)

while len(personal) > 0:
    del personal[0]
    input()


'''
Гугл и stack overflow говорят, что в питоне нет встроенной функции, которая возврщала бы список всех объектов 
класса. Для этого рекомендуют явно создавать этот список самостоятельно. Либо так, как реализовано в этом коде
в конструкторе класса, либо через self.__class__.personal.append(self).
Я пытался выносить список personal в пространство имён main, потому что не нравилось, что все объекты класса
наследуют список personal как атрибут родителя, и в дебаггере попытка посмотреть атрибуты объектов класса вообще
выглядит как бесконечная рекурсия при просмотре списка personal. Но вынос за пространство имён класса мне понра-
вилось ещё меньше: хоть объекты (очевидно) не наследуют поле в виде  листа personal, интерпретатор ругается, что
я в лист добавляю объекты класса объект, и я считал, что отсутствие списка объектов в классе - причина удаления
объектов класса в "неотсортированном" порядке. Но последняя проблема наблюдается и при размещении списка внутри
класса.
При текущей реализации я могу отсортировать список объектов по параметру qual, также могу их удалить по порядку,
использую метод __del__ класса Person. Но потом интерпретатор удаляет их в "неотсортированном порядке". Есть по-
дозрение, что переопределённый метод только печатает строку, не удаляя объект. Нужно как-то дописать переопреде-
лённый метод __del__ класса Person, чтобы функциональность удаления появилась. - Нет, в пособии __del__(Person) 
содержит только print(....). 
Пособие говорит, что "если в программе имеется несколько ссылок-переменных  на объект, удаление одной из них не
приведёт к удалению объекта и вызову деструктора". 
Единственный рабочий метод - создать спсок вне класса и туда добавлять объекты класса вручную, а не через конс-
труктор, затем удаляя элементы в отсортированном списке объектов через обращение по индексу: del personal[x]. 
Если же вызывать деструктор, объект не удаляется из памяти (где-то остаётся ссылка на него) - а оно и не надо 
при такой реализации.
Если список объявлен внутри класса, а объекты в него добавляются при помощи конструктора класса, то при попытке
удалять элементы по индексам из списка удаляет элементы списка, но не удаляет сами элементы (логично).

'''