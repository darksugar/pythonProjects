#Authon Ivor
from core import db_handler

class Class_Manage(object):
    def __init__(self,user_data):
        menu = '''
        1.  添加班级
        2.  添加学员到班级
        3.  查看学员
        '''
        menu_dic = {
            '1':self.add_class,
            '2':self.add_student2class,
            '3':self.get_stu_class,
        }
        print(menu)
        choice = input("[1/2]>>>:")
        if choice.isdigit():
            menu_dic.get(choice)(user_data)

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

    def add_class(self,user_data):
        class_name = input("Input the class name:")
        db_api = self.db_conn()
        res = db_api.add_class(class_name,user_data["account_data"].tea_id)
        if res:
            print("Class %s added..." % class_name)

    def add_student2class(self,user_data):
        db_api = self.db_conn()
        class_obj = db_api.get_all_class()
        for class_id,class_name in class_obj:
            print("Class id:%s Class name:%s " % (class_id,class_name))
        student_obj = db_api.get_all_student()
        class_name = input("Input the class name:")
        for stu_id,stu_name,qq in student_obj:
            print("Student id:%s Student Name:%s Student qq:%s" % (stu_id,stu_name,qq))
        qq_num = input("Input the qq of student:")

        res = db_api.add_student2class(class_name,qq_num)
        if res:
            print("Student added...")

    def get_stu_class(self,user_data):
        db_api = self.db_conn()
        obj = db_api.get_class_student()
        for i in obj:
            print("Student Name:%s Class Name:%s" % (i.stu.stu_name,i.classes.class_name))

class Class_record_Manage(object):
    def __init__(self, user_data):
        menu = '''
        1.  添加上课记录
        '''
        menu_dic = {
            '1': self.add_class_record,
        }
        print(menu)
        choice = input("[1]>>>:")
        if choice.isdigit():
            menu_dic.get(choice)(user_data)

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

    def add_class_record(self,user_data):
        class_name = input("Input the class name:")
        lesson_name = input("Input the lesson name:")
        db_api = self.db_conn()
        res = db_api.add_class_record(class_name,lesson_name,user_data["account_data"].tea_id)
        if res:
            print("Record added...")

class Score_Manage(object):
    def __init__(self, user_data):
        menu = '''
        1.  修改成绩
        '''
        menu_dic = {
            '1': self.change_score
        }
        print(menu)
        choice = input("[1]>>>:")
        if choice.isdigit():
            menu_dic.get(choice)(user_data)

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

    def change_score(self,user_data):
        class_name = input("Input class name:")
        lesson_name = input("Input lesson name:")
        db_api = self.db_conn()
        id_list = db_api.get_score(user_data["account_data"].tea_id,lesson_name,class_name)
        if not id_list:return
        for count in range(len(id_list)):
            stu_id = input("Input the student id:")
            score = input("Input the  Score:")
            if int(stu_id) not in id_list:
                print("Wrong ID...")
                continue
            res = db_api.change_score(stu_id,lesson_name,score)
            if res:
                print("Chang success...")