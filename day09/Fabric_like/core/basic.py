#Authon Ivor
import os
import pickle
import paramiko
from conf import settings

class Host(object):
    def __init__(self,name,ip,port,username,password,group):
        self.id = settings.get_new_id()
        self.name = name
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.group = group
    def add_new(self):
        with open("%s/%s" % (settings.HOST_DIR, self.id),'wb') as f:
            pickle.dump(self,f)
        if os.path.isfile("%s/%s" % (settings.HOST_DIR, self.id)):
            return True
        else:
            return False
    def update(self):
        with open("%s/%s" % (settings.HOST_DIR, self.id),'wb') as f:
            pickle.dump(self,f)
        if os.path.isfile("%s/%s" % (settings.HOST_DIR, self.id)):
            return True
        else:
            return False
    def make_connect(self):
        transport = paramiko.Transport((self.ip,self.port))
        transport.connect(username=self.username, password=self.password)
        return transport

    def ssh_execute_cmd(self,cmd,output=True):
        transport = self.make_connect()
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        error = stderr.read()
        if output :
            print("%s result".center(50,"-") % self.name)
            print(result.decode() if result else error.decode())
        transport.close()

class Group(object):
    def __init__(self,groupname):
        self.id = settings.get_new_id()
        self.name = groupname
        self.hosts_list = []
    def add_new(self):
        with open("%s/%s" % (settings.GROUP_DIR, self.id),'wb') as f:
            pickle.dump(self,f)
        if os.path.isfile("%s/%s" % (settings.GROUP_DIR, self.id)):
            return True
        else:
            return False
    def update(self):
        print(self)
        with open("%s/%s" % (settings.GROUP_DIR, self.id), 'wb') as f:
            pickle.dump(self, f)
        if os.path.isfile("%s/%s" % (settings.GROUP_DIR, self.id)):
            return True
        else:
            return False