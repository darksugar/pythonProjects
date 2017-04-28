#Authon Ivor
import os,stat
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
            f.flush()
        if os.path.isfile("%s/%s" % (settings.HOST_DIR, self.id)):
            return True
        else:
            return False
    def change_attr(self,attr):
        if hasattr(self,attr):
            new_detail = input("Input the %s:" % attr)
            setattr(self,attr,new_detail)
            res = self.update()
            if res:
                return attr
        else:
            return False
    def update(self):
        with open("%s/%s" % (settings.HOST_DIR, self.id),'wb') as f:
            pickle.dump(self,f)
            f.flush()
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
    def sftp_put_file(self,local_file_path,remote_path):
        transport = self.make_connect()
        sftp = paramiko.SFTPClient.from_transport(transport)
        if os.path.isfile(local_file_path):
            if remote_path.endswith("/"):
                remote_path = remote_path + local_file_path.split(os.sep)[-1]
            else:
                remote_path = remote_path + "/" + local_file_path.split(os.sep)[-1]
            try:
                sftp.put(local_file_path,remote_path)
            except FileNotFoundError:
                print("\033[31;1mRemote Dir is not exists:\033[0m")
            except Exception as e:
                print(e)
            else:
                print("\033[32;1mFile put done...\033[0m")
                transport.close()
        if os.path.isdir(local_file_path):
            if remote_path.endswith("/"):
                remote_dir = remote_path + local_file_path.split(os.sep)[-1]
            else:
                remote_dir = remote_path + "/" +local_file_path.split(os.sep)[-1]
            try:
                sftp.mkdir(remote_dir)
            except FileNotFoundError:
                    sftp.mkdir(remote_path)
                    sftp.mkdir(remote_dir)
                    print("\033[32;1mCreate Dir %s\033[0m" % remote_path)
                    print("\033[32;1mCreate Dir %s\033[0m" % remote_dir)
            else:
                print("\033[32;1mCreate Dir %s\033[0m" % remote_dir)
            for cur_dir,dir_list,file_list in os.walk(local_file_path):
                for file_name in file_list:
                    remote_file_name = remote_dir + "/" + file_name
                    local_file_name = os.path.join(cur_dir,file_name)
                    try:
                        sftp.put(local_file_name,remote_file_name)
                    except FileNotFoundError:
                        print("\033[31;1mRemote Dir is not exists:\033[0m")
                    except Exception as e:
                        print(e)
                    else:
                        print("\033[32;1mDir put done...\033[0m")
        transport.close()
    def sftp_get_file(self, remote_path):
        transport = self.make_connect()
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.listdir_attr()



class Group(object):
    def __init__(self,groupname):
        self.id = settings.get_new_id()
        self.name = groupname
        self.hosts_list = []
    def add_new(self):
        with open("%s/%s" % (settings.GROUP_DIR, self.id),'wb') as f:
            pickle.dump(self,f)
            f.flush()
        if os.path.isfile("%s/%s" % (settings.GROUP_DIR, self.id)):
            return True
        else:
            return False
    def add_host(self,add_host):
        self.hosts_list.append(add_host)
        res = self.update()
        if res:
            return True
    def remove_host(self,rm_host):
        for host in self.hosts_list:
            if host.name == rm_host.name:
                self.hosts_list.remove(host)
                res = self.update()
                if res:
                    return True
    def update(self):
        with open("%s/%s" % (settings.GROUP_DIR, self.id), 'wb') as f:
            pickle.dump(self, f)
            f.flush()
        if os.path.isfile("%s/%s" % (settings.GROUP_DIR, self.id)):
            return True
        else:
            return False