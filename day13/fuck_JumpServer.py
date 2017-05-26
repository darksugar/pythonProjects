#Authon Ivor
from sqlalchemy import Column,String,ForeignKey,UniqueConstraint,Integer,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

host_m2m_remoteuser = Table('host_m2m_remoteuser', Base.metadata,
                        Column('host_id',Integer,ForeignKey('host.hid')),
                        Column('remoteuser_id',Integer,ForeignKey('remoteuser.id')),
                        )

class Host(Base):
    __tablename__ = 'host'
    hid = Column(Integer,primary_key=True,autoincrement=True)
    host_name = Column(String(32),nullable=True,unique=True)
    ip = Column(String(16),nullable=True)
    port = Column(String(8),nullable=True)
    remote_users = relationship('RemoteUser',secondary=host_m2m_remoteuser,backref='hosts')

    def __repr__(self):
        return self.host_name

class HostGroup(Base):
    __tablename__ = 'hostgroup'
    gid = Column(Integer,primary_key=True,autoincrement=True)
    group_name = Column(String(32),nullable=True)

class UserProfile(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(16),nullable=True)
    password = Column(String(16),nullable=True)

class RemoteUser(Base):
    __table__ = 'remoteuser'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(16),nullable=True)
    password = Column(String(16),nullable=True)
    auth_type = Column(String(8),nullable=True)

class AuditLog(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    cmd = Column(String(16),nullable=True)
    local_user = Column(String(16),nullable=True)
    remote_user = Column(String(16),nullable=True)