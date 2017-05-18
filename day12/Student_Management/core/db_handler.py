#Authon Ivor
from core.basic import Student, Teacher, Class, Stu_Class_Realationship, Class_record, Student_record
from conf import settings
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

class db_handler(object):
    def __init__(self):
        engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % \
          (settings.db_user, settings.db_pass, settings.db_ip, settings.db_port, settings.db_name))
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def teacher_auth(self,username):
        teacher = self.session.query(Teacher).filter_by(username=username).first()
        return teacher

    def student_auth(self,username):
        student = self.session.query(Student).filter_by(username=username).first()
        return student

    def get_class(self,class_name):
        class_obj = self.session.query(Class).filter_by(class_name=class_name).first()
        return class_obj

    def get_student_byqq(self,qq):
        student_obj = self.session.query(Student).filter_by(qq=qq).first()
        return student_obj

    def add_class(self,class_name,tea_id):
        class_obj = self.get_class(class_name)
        if class_obj:return print("Class exists...")
        class_obj = Class(class_name=class_name,tea_id=tea_id)
        self.session.add(class_obj)
        self.session.commit()
        return True

    def add_student2class(self,class_name,qq_num):
        class_obj = self.get_class(class_name)
        if not class_obj: return print("Wrong class name...")
        student_obj = self.get_student_byqq(qq_num)
        if not student_obj:return print("Wrong qq number...")
        relation_obj = Stu_Class_Realationship(stu_id=student_obj.stu_id,class_id=class_obj.class_id)
        self.session.add(relation_obj)
        self.session.commit()
        return True

    def add_class_record(self,class_name,lesson_name,tea_id):
        class_obj = self.get_class(class_name)
        if not class_obj: return print("Wrong class name...")
        class_record_obj = Class_record(lesson_name=lesson_name,class_id=class_obj.class_id,tea_id=tea_id)
        self.session.add(class_record_obj)
        self.add_student_record(class_obj.class_id,lesson_name)
        self.session.commit()
        return True

    def add_student_record(self,class_id,lesson_name):
        res = self.session.query(Stu_Class_Realationship).filter_by(class_id=class_id).all()
        for re_obj in res:
            student_record_obj = Student_record(stu_id=re_obj.stu_id,class_id=class_id,lesson_name=lesson_name)
            self.session.add(student_record_obj)