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
    __tablename__ = "users"
    stu_id = Column(Integer, primary_key=True)
    stu_name = Column(String(16))
    username = Column(String(16))
    password = Column(String(16))
    qq = Column(String(16))

    def __repr__(self):
        return "%s-%s-%s" % (self.stu_id, self.name, self.qq)

class Teacher(Base):
    __tablename__ = "teachers"
    tea_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(16))
    username = Column(String(16))
    password = Column(String(16))
    qq = Column(String(16))

    def __repr__(self):
        return "%s-%s" % (self.tea_id, self.teacher_name)

class Class(Base):
    __tablename__ = "classes"
    class_id = Column(Integer, primary_key=True)
    class_name = Column(String(32))
    tea_id = Column(Integer)
    stu_num = Column(Integer)

    def __repr__(self):
        return "%s-%s-%s" % (self.class_id, self.class_name, self.tea_id)

class Stu_Class_Realationship(Base):
    __tablename__ = "stu_class_relationship"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer)
    class_id = Column(Integer)

    def __repr__(self):
        return "%s-%s" % (self.stu_id, self.class_id)

class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer)
    class_id = Column(Integer)
    submit_type = Column(Integer,default=0)
    score = Column(Integer)

    def __repr__(self):
        return "%s-%s" % (self.stu_id, self.class_id)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()