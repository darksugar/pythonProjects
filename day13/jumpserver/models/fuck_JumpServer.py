#Authon Ivor
from sqlalchemy import Column,String,ForeignKey,UniqueConstraint,Integer,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType


Base = declarative_base()

userprofile_m2m_bindhost = Table('userprofile_m2m_bindhost', Base.metadata,
                        Column('userprofile_id',Integer,ForeignKey('userprofile.uid')),
                        Column('bindhost_id',Integer,ForeignKey('bindhost.bindid')),
                        )
bindhost_m2m_hostgroup = Table('host_m2m_remoteuser', Base.metadata,
                        Column('bindhost_id',Integer,ForeignKey('bindhost.bindid')),
                        Column('hostgroup_Id',Integer,ForeignKey('hostgroup.gid')),
                        )
userprofile_m2m_hostgroup = Table('userprofile_m2m_hostgroup', Base.metadata,
                        Column('userprofile_id',Integer,ForeignKey('userprofile.uid')),
                        Column('hostgroup_Id',Integer,ForeignKey('hostgroup.gid')),
                        )

class Host(Base):
    '''
    主机表
    '''
    __tablename__ = 'host'
    hid = Column(Integer,primary_key=True,autoincrement=True)
    host_name = Column(String(32),nullable=True,unique=True)
    ip = Column(String(16),nullable=True)
    port = Column(Integer,nullable=True)

    def __repr__(self):
        return self.host_name

class RemoteUser(Base):
    '''
    远程主机用户表
    '''
    __tablename__ = 'remoteuser'
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password', name='_user_passwd_uc'),)
    AuthTypes = [
        (u'ssh-passwd', u'SSH/Password'),
        (u'ssh-key', u'SSH/KEY'),
    ]

    ruid = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(16),nullable=True)
    password = Column(String(16),nullable=True)
    # auth_type = Column(String(8),nullable=True)
    auth_type = Column(ChoiceType(AuthTypes))

class BindHost(Base):
    '''
    绑定主机和远程用户
    relationship:
        host:查询绑定的主机
        remoteuser:查询远程用户
    '''
    __tablename__ = 'bindhost'
    __table_args__ = (UniqueConstraint('host_id','remoteuser_id', name='remoteuser_host_unique'),)

    bindid = Column(Integer,primary_key=True,autoincrement=True)
    host_id = Column(Integer,ForeignKey('host.hid'))
    remoteuser_id = Column(Integer,ForeignKey('remoteuser.ruid'))

    host = relationship('Host',foreign_keys=[host_id],backref='bindhost')
    remoteuser = relationship('RemoteUser',foreign_keys=[remoteuser_id],backref='bindhost')

class HostGroup(Base):
    '''
    主机组
    relationship:
        bindhost:组绑定的主机
    '''
    __tablename__ = 'hostgroup'
    gid = Column(Integer,primary_key=True,autoincrement=True)
    group_name = Column(String(32),nullable=True)

    bindhost = relationship('BindHost',secondary=bindhost_m2m_hostgroup,backref='hostgroup')

    def __repr__(self):
        return self.group_name

class UserProfile(Base):
    '''
    堡垒机用户
    relationship:
        bindhost:绑定的单台主机
        hostgroup:绑定的主机组
    '''
    __tablename__ = 'userprofile'
    uid = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(16),nullable=True)
    password = Column(String(16),nullable=True)

    bindhost = relationship('BindHost',secondary=userprofile_m2m_bindhost,backref='userprofile')
    hostgroup = relationship('HostGroup',secondary=userprofile_m2m_hostgroup,backref='userprofile')

    def __repr__(self):
        return self.username

class AuditLog(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    cmd = Column(String(16),nullable=True)
    local_user = Column(String(16),nullable=True)
    remote_user = Column(String(16),nullable=True)

if __name__ == '__main__':
    def init_db():
        Base.metadata.create_all(engine)
    def drop_db():
        Base.metadata.drop_all(engine)

    engine = create_engine("mysql+pymysql://root:mysql123@127.0.0.1:3306/test", max_overflow=5)
    Session = sessionmaker(bind=engine)
    session = Session()
    drop_db()
    init_db()
