#Authon Ivor
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
import os,sys
Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_Dir)
from conf import settings

engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % \
         (settings.db_user, settings.db_pass, settings.db_ip, settings.db_port, settings.db_name))
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    stu_id = Column(Integer, primary_key=True, nullable=False)
    stu_name = Column(String(16))
    username = Column(String(16),unique=True)
    password = Column(String(16))
    qq = Column(String(16),unique=True)
    expire_date = Column(String(16))
    status = Column(Integer)

    def __repr__(self):
        return "%s-%s-%s" % (self.stu_id, self.stu_name, self.qq)

class Teacher(Base):
    __tablename__ = "teachers"
    tea_id = Column(Integer, primary_key=True, nullable=False)
    teacher_name = Column(String(16))
    username = Column(String(16),unique=True)
    password = Column(String(16))
    qq = Column(String(16),unique=True)
    expire_date = Column(String(16))
    status = Column(Integer)

    def __repr__(self):
        return "%s-%s" % (self.tea_id, self.teacher_name)

class Class(Base):
    __tablename__ = "classes"
    class_id = Column(Integer, primary_key=True, nullable=False)
    class_name = Column(String(32),unique=True)
    tea_id = Column(Integer)
    stu_num = Column(Integer, default=0)

    def __repr__(self):
        return "%s-%s-%s" % (self.class_id, self.class_name, self.tea_id)

class Stu_Class_Realationship(Base):
    __tablename__ = "stu_class_relationship"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer, nullable=False)
    class_id = Column(Integer, nullable=False)

    def __repr__(self):
        return "%s-%s" % (self.stu_id, self.class_id)

class Student_record(Base):
    __tablename__ = "record_student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer, nullable=False)
    class_id = Column(Integer, nullable=False)
    lesson_name = Column(String(32))
    submit_type = Column(Integer,default=0)
    score = Column(Integer)

    def __repr__(self):
        return "%s-%s" % (self.stu_id, self.class_id)

class Class_record(Base):
    __tablename__ = "record_class"
    lesson_id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_name = Column(String(32))
    class_id = Column(Integer, nullable=False)
    tea_id = Column(Integer, nullable=False)

    def __repr__(self):
        return "%s-%s" % (self.stu_id, self.class_id)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# drop_db()
# init_db()
# teacher = Teacher(teacher_name = 'ivor',
#                   username = 'ivor',
#                   password = 'ivor',
#                   qq =321,
#                   expire_date ='20171111',
#                   status = 0
#                   )
# student1 = Student(stu_name = 'foo',
#                   username = 'foo',
#                   password = 'foo',
#                   qq =123,
#                   expire_date ='20171111',
#                   status = 0
#                   )
# student2 = Student(stu_name = 'coo',
#                   username = 'coo',
#                   password = 'coo',
#                   qq =1234,
#                   expire_date ='20171111',
#                   status = 0
#                   )
# student3 = Student(stu_name = 'too',
#                   username = 'too',
#                   password = 'too',
#                   qq =12345,
#                   expire_date ='20171111',
#                   status = 0
#                   )
# session.add_all(
#     [teacher,student1,student2,student3]
# )
# session.commit()