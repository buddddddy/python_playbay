from teacher_students_task import *


lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marivanna = Teacher()
vasy = Pupil()
pety = Pupil()
marivanna.teach(lesson[2], vasy, pety)
marivanna.teach(lesson[0], pety)
print(vasy.knowledge)
print(pety.knowledge)

vasy.take(lesson[0])  # ability for self-education
print(vasy.knowledge)

vasy.forget_smth()

print(vasy.knowledge)

