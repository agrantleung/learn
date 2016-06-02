#class Student(object):

#    def get_score(self):
#         return self._score

#    def set_score(self, value):
#        if not isinstance(value, int):
#            raise ValueError('score must be an integer!')
#        if value < 0 or value > 100:
#            raise ValueError('score must between 0 ~ 100!')
#       self._score = value

#s=Student()
#s.set_score(74)
#print(s.get_score())

##############################
# @property把方法变成属性
##############################
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('ssssscore must be an integer!!!')
        if value < 0 or value > 100:
            raise ValueError('ssssscore must between 0~100!!!')
        self._score = value

#s = Student()
Student.score = 20
print(Student.score)


class screen(object):
    @property
    def f(self):
        return self.w, self.h
    @f.setter
    def f(self,weight,height):
        self.w=weight
        self.h=height
    @property
    def resolution(self):
        return self.w * self.h

s=screen()
s.w=1024
s.h=768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution