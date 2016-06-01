class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s ' % (self.__name, self.__score))
    def get_grade(self):
        if self.__score >= 90:
            print('A')
        elif self.__score >= 60:
            print('B')
        else:
            print('C')
    def get_name(self):
        print (self.__name)
    def get_score(self):
        print (self.__score)
    def set_score(self, score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bbbbbad ssssscore')


bart = Student('Bart Simpsion', 98)

bart.print_score()
bart.get_grade()
bart.get_name()
bart.get_score()
bart.set_score(4)
bart.print_score()
print(bart._Student__name)