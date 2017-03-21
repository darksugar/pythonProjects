#Authon Ivor
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core.basic import School,Course,Classes,Teacher,Student
from db.load_data import load

data = load()

def create_student():
    #输入姓名，年龄，学校，班级
    name = input("input your name:")
    age = input("input your age:")
    #打印学校列表
    for i,v in enumerate(data["school_list"]):
        print(i,v.name)
    school = int(input("Choose your school:"))
    #打印班级列表
    for i,v in enumerate(data["classes_list"]):
        print(i,v.name)
    classes = int(input("Choose your classes:"))
    #将新对象加入data
    student = Student(name,age,data["school_list"][school],data["school_list"][classes])
    data["student_list"].append(student)

def pay_fee():
    #打印学生列表
    for i,v in enumerate(data["student_list"]):
        print(i,v.name)
    choice = int(input("Choose the student your want pay:"))
    #调用学生的缴费函数
    data["studnt_list"][choice].pay()
    print("%s 's amount is %s now." % (data["student_list"][choice].name,data["student_list"][choice].amount))

def choose_classes():
    #打印学生列表
    for i,v in enumerate(data["student_list"]):
        print(i,v.name)
    student = int(input("Choose the student your want change:"))
    print("%s 's classes is %s . " % (data["student_list"][student].name,data["student_list"][student].classes.name))
    #打印班级列表
    for i,v in enumerate(data["classes_list"]):
        print(i,v.name)
    classes = int(input("Choose the classes your want change:"))
    #调用学生的更改班级函数
    data["student_list"][student].change_classes(data["classes_list"][classes])
    print("%s 's classes is %s now." % (data["student_list"][student].name, data["student_list"][student].classes.name))

def choose_course():
    for i,v in enumerate(data["student_list"]):
        print(i,v.name)
    stu = int(input("Choose the student:"))
    for i,v in enumerate(data["student_list"][stu].classes.course_list):
        print(i,v.name)
    course = int(input("Please input course:"))
    data["student_list"][stu].score.add_course(data["student_list"][stu].classes.course_list[i].name)




def stu_api():
    menu = '''
    1. 新学员注册
    2. 学员缴费
    3. 选择班级
    4. 上课
    '''
    menu_dic = {
        1:create_student,
        2:pay_fee,
        3:choose_classes,
        4:choose_course
    }
    print(menu)
    choice = int(input("Please input:"))
    menu_dic[choice]()

def query_stu():
    for i,v in enumerate(data["teacher_list"]):
        print(i,v.name)
    teacher = int(input("Please choose the teacher:"))
    print("%s 的学员 " % data["teacher_list"][teacher].classes.name)
    for stu in data["teacher_list"][teacher].classes.stu_list:
        print(stu.name)

def add_score():
    for i,v in enumerate(data["teacher_list"]):
        print(i,v.name)
    teacher = int(input("Please choose the teacher:"))
    print("%s 的学员 " % data["teacher_list"][teacher].classes.name)
    for index, course in enumerate(data["teacher_list"][teacher].classes.course_list):
        print(index, course.name)
    course = int(input("Choose the course:"))


def change_score():
    for i,v in enumerate(data["teacher_list"]):
        print(i,v.name)
    teacher = int(input("Please choose the teacher:"))
    print("%s 的学员 " % data["teacher_list"][teacher].classes.name)
    for index,stu in enumerate(data["teacher_list"][teacher].classes.stu_list):
        print(index,stu.name)
    stu = int(input("Choose the student:"))
    if data["teacher_list"][teacher].classes.stu_list[stu].score:
        for i,v in enumerate(data["teacher_list"][teacher].classes.stu_list[stu].score.score.item()):
            print(i,v)
    else:
        print("该学生没有成绩.")

def tea_api():
    menu = '''
    1. 查看学员列表
    2.
    3. 修改学员成绩
    '''
    menu_dic = {
        1:query_stu,
        2:add_score,
        3:change_score
    }
    print(menu)
    choice = int(input("Please input your choice:"))
    menu_dic[choice]()


def manage_api():
    pass



def run():
    menu = '''
    1. 学员入口
    2. 老师入口
    3. 管理入口
    4. 退出程序
    '''
    menu_dic = {
        1:stu_api,
        2:tea_api,
        3:manage_api,
        4:exit
    }
    while True:
        print(menu)
        choice = int(input("Please input:"))
        menu_dic[choice]()

run()