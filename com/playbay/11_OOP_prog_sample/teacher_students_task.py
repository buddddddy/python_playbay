from random import choice


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, item):
        return self.info[item]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget_smth(self):
        if len(self.knowledge) != 0:
            self.knowledge.remove(choice(self.knowledge))
