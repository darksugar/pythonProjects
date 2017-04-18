#Authon Ivor
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core.basic import School,Course,Classes,Teacher,Student
from db.load_data import load,dump
import pickle
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
    data["student_list"][stu].score.add_course(data["student_list"][stu].classes.course_list[course].name)

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
def query_score():
    for i,v in enumerate(data["teacher_list"]):
        print(i,v.name)
    teacher = int(input("Please choose the teacher:"))
    for index, stu in enumerate(data["teacher_list"][teacher].classes.stu_list):
        print(index, stu.name)
    stu = int(input("Choose the course:"))
    for course, score in data["teacher_list"][teacher].classes.stu_list[stu].score.score.items():
        print(course,score)
def change_score():
    for i,v in enumerate(data["teacher_list"]):
        print(i,v.name)
    teacher = int(input("Please choose the teacher:"))
    print("%s 的学员 " % data["teacher_list"][teacher].classes.name)
    for index,stu in enumerate(data["teacher_list"][teacher].classes.stu_list):
        print(index,stu.name)
    stu = int(input("Choose the student:"))
    if data["teacher_list"][teacher].classes.stu_list[stu].score:
        for i,v in data["teacher_list"][teacher].classes.stu_list[stu].score.score.items():
            print(i,v)
        course = input("input the course:")
        score = int(input("input the score:"))
        data["teacher_list"][teacher].classes.stu_list[stu].score.score[course] = score
    else:
        print("该学生没有成绩.")

def tea_api():
    menu = '''
    1. 查看学员列表
    2. 查看学员成绩
    3. 修改学员成绩
    '''
    menu_dic = {
        1:query_stu,
         2:query_score,
        3:change_score
    }
    print(menu)
    choice = int(input("Please input your choice:"))
    menu_dic[choice]()

def create_classes():
    for i, v in enumerate(data["school_list"]):
        print(i, v.name)
    school = int(input("请选择新班级所属学校:"))
    classes_name = input("请输入新班级名称:")
    classes = Classes(data["school_list"][school],classes_name)
    data["classes_list"].append(classes)
def create_teacher():
    for i, v in enumerate(data["school_list"]):
        print(i, v.name)
    school = int(input("请选择新老师所属学校:"))
    for i, v in enumerate(data["classes_list"]):
        print(i, v.name)
    classes = int(input("请选择新老师所属学校:"))
    teacher_name = input("请输入新老师姓名:")
    teacher_age = input("请输入新老师年龄:")
    teacher = Teacher(teacher_name,teacher_age,data["school_list"][school], data["clasees_list"][classes])
    data["teacher_list"].append(teacher)
def create_course():
    for i,v in enumerate(data["school_list"]):
        print(i,v.name)
    school = int(input("请选择新课程所属学校:"))
    course_name = input("请输入课程名称:")
    course_outline = input("请输入课程周期:")
    course_price = int(input("请输入课程价格:"))
    course = Course(data["school_list"][school],course_name,course_outline,course_price)
    data["course_list"].append(course)
def conn_course_classes():
    for i, v in enumerate(data["classes_list"]):
        print(i, v.name)
    classes = int(input("请选择要关联的班级:"))
    for i, v in enumerate(data["course_list"]):
        if data["course_list"][i].school == data["classes_list"][classes].school:
            print(i, v.name)
    course = int(input("请选择要关联的课程:"))
    data["classes_list"][classes].add_course(data["course_list"][course])

def manage_api():
    menu = '''
        1. 创建课程
        2. 创建班级
        3. 创建老师
        4. 关联班级课程
        '''
    menu_dic = {
        1: create_course,
        2: create_classes,
        3: create_teacher,
        4:conn_course_classes
    }
    print(menu)
    choice = int(input("Please input your choice:"))
    menu_dic[choice]()

def dump_data():
    dump(data)
    exit()

def run():
    menu = '''
    1. 学员入口
    2. 老师入口
    3. 管理入口
    4. 退出程序(保存现有数据)
    '''
    menu_dic = {
        1:stu_api,
        2:tea_api,
        3:manage_api,
        4:dump_data
    }
    while True:
        print(menu)
        choice = int(input("Please input:"))
        menu_dic[choice]()
run()