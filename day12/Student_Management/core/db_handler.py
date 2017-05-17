#Authon Ivor
from core.basic import Student, Teacher, Class, Stu_Class_Realationship, Score
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




