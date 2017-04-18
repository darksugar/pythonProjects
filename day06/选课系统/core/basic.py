#Authon Ivor
import pickle

class School(object):
    def __init__(self,name,city):
        self.name = name
        self.city = city

class Course(object):
    def __init__(self,school,name,outline,price):
        self.school = school
        self.name = name
        self.cycle = outline
        self.price = price

class Classes(object):
    def __init__(self,school,name):
        self.school = school
        self.name = name
        self.stu_list = []
        self.course_list = []
    def add_course(self,course):
        self.course_list.append(course)

class People(object):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school =school

class Teacher(People):
    def __init__(self, name,age,school,classes):
        super(Teacher, self).__init__(name,age,school)
        self.classes = classes

class Student(People):
    def __init__(self, name,age,school,classes):
        super(Student, self).__init__(name,age,school)
        self.classes = classes
        self.amount = 0
        self.score = Score()
    def pay(self):
        self.amount += int(input("Please input the amount:"))
    def change_classes(self,classes):
        self.classes = classes

class Score(object):
    def add_course(self,course):
        self.score = {
        course:0
        }
    def set_score(self,course,score):
        self.score = {
            course: score
        }


def create_school():
    pass

def create_course():
    pass

def create_classes():
    pass



