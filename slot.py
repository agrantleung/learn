class Student(object):
    __slots__=('name','age')
s = Student()
s.name = 'Micheal'
print(s.name)

def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(99)
print(s.score)

s2=Student()
s2.set_score(85)
print(s2.score)

class GraduateStudent(Student):
    __slots__ = ('score',)
g= GraduateStudent()
g.score=88
print(g.score)