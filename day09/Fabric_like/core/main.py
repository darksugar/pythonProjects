#Authon Ivor
import pickle
import re,os,sys
import threading
import logging
from core import basic
from conf import settings

class Fabric_like(object):
    def __init__(self):
        self.logger = self.get_logger()

    def get_logger(self):
        '''
        创建日志对象
        '''
        logger = logging.getLogger()
        logger.setLevel(settings.LOG_LEVEL)
        file_handler = logging.FileHandler(settings.LOG_FILE)
        fh_formatter = logging.Formatter("%(asctime)s  %(levelname)s  %(name)s  %(message)s")
        file_handler.setFormatter(fh_formatter)
        logger.addHandler(file_handler)
        return logger

    def start(self):
        '''
        交互菜单
        '''
        menu = '''
            1. Print Host List
            2. Print Group List
            3. Execute CMD
            4. Put File
            5. Get File
            6. Add New Host
            7. Add New Group
            8. Change Host Detail
            '''
        menu_dic = {
            1:self.print_list,
            2:self.print_group,
            3:self.execute_cmd,
            4:self.put_file,
            5:self.get_file,
            6:self.add_host,
            7:self.add_group,
            8:self.change_host
        }
        while True:
            choice = input("Input the Number(help[0])>>:")
            if choice == '0':
                print(menu)
                continue
            if choice.isdigit():
                choice = int(choice)
                if  0 < choice < (len(menu_dic)+1):
                    menu_dic[choice]()
                else:
                    print("\033[31;1mChoice out of range...\033[0m")
            else:
                print("\033[31;1mChoice must a NUM...\033[0m")

    def active_hosts(self):
        '''
        将选中的主机添加到self.host_obj_list
        '''
        host_dic = self.print_list()
        self.host_obj_list = []
        example = '''
        Input the host name
        Choose one host:host1
        Choose multipule host:host1,host2,host3
        '''
        print(example)
        choice = input(">>>:")
        host_list = choice.strip().split(",")
        for host in host_list:
            if host in host_dic.keys():
                self.host_obj_list.append(host_dic.get(host))
            else:
                print("\033[31;1mWrong Input...\033[0m")
                return False
        print(host_list)
        return True

    def active_group(self):
        '''
        将选中的组添加到self.group_obj_list
        '''
        group_dic = self.print_group()
        self.group_obj_list = []
        example = '''
        Input the groups name
        Choose one groups:group1
        Choose multipule groups:group1,group2,group3
        '''
        print(example)
        choice = input(">>>:")
        group_list = choice.strip().split(",")
        for group_name in group_list:
            if group_name in group_dic.keys():
                self.group_obj_list.append(group_dic.get(group_name))
            else:
                print("\033[31;1mWrong Input...\033[0m")
                return False
        print(group_list)
        return True

    def print_list(self,out_put=True):
        '''
        打印主机列表,返回主机字典
        { host_obj.name: host_obj }
        '''
        host_dic = {}
        for host_file in os.listdir(settings.HOST_DIR):
            with open("%s/%s" % (settings.HOST_DIR,host_file),"rb") as host:
                host_obj = pickle.load(host)
                host_dic[host_obj.name] = host_obj
                if out_put:
                    print("Host:%s:%s(%s:%s):" % (host_obj.name,host_obj.group,host_obj.ip,host_obj.port))
        return host_dic

    def print_group(self,out_put=True):
        '''
        打印组列表,返回组字典
        { group_obj.name: group_obj }
        '''
        group_list = {}
        for group_file in os.listdir(settings.GROUP_DIR):
            with open("%s/%s" % (settings.GROUP_DIR,group_file),"rb") as group:
                group_obj = pickle.load(group)
                group_list[group_obj.name] = group_obj
                if out_put:
                    print("Group:%s" % group_obj.name)
                    for host in group_obj.hosts_list:
                        print("\thost:%s" % host.name)
        return group_list

    def execute_cmd(self):
        '''
        对选中的主机或者组执行命令
        多线程
        '''
        menu = '''
        1. Choose Host[s]
        2. Choose Group
        '''
        print(menu)
        choice = input("[1/2]>>>:")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                if self.active_hosts():
                    cmd = input("Input CMD:")
                    thread_list = []
                    for host in self.host_obj_list:
                        t = threading.Thread(target=host.ssh_execute_cmd,args=(cmd,))
                        t.setDaemon(True)
                        thread_list.append(t)
                        t.start()
                        self.logger.info("Execute CMD '%s' to host:%s" % (cmd,host.name))
                    for t in thread_list:
                        t.join()

            elif choice == 2:
                if self.active_group():
                    cmd = input("Input CMD:")
                    thread_list = []
                    for group in self.group_obj_list:
                        print("Group:%s".center(50,"=") % group.name)
                        for host in group.hosts_list:
                            t = threading.Thread(target=host.ssh_execute_cmd, args=(cmd,))
                            t.setDaemon(True)
                            thread_list.append(t)
                            t.start()
                            self.logger.info("Execute CMD '%s' to host:%s" % (cmd, host.name))
                    for t in thread_list:
                        t.join()
            else:
                print("\033[31;1mWrong Number\033[0m")
        else:
            print("\033[31;1mChoice must a Number...\033[0m")

    def GetFileList(self,dir, fileList,dirList):
        '''
        返回目录的文件列表和目录列表
        '''
        newDir = dir
        if os.path.isfile(dir):
            fileList.append(dir)
        elif os.path.isdir(dir):
            dirList.append(dir)
            for s in os.listdir(dir):
                # 忽略某些文件夹
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.GetFileList(newDir, fileList,dirList)
        return fileList,dirList

    def put_file(self):
        '''
        文件或者文件夹放在tmp目录下
        本地文件名或文件夹名直接输入名字,如:test.file|testdir
        远程路径输入文件夹的名字，如:/tmp
        目前不支持重命名
        '''
        menu = '''
                1. Choose Host[s]
                2. Choose Group
                '''
        print(menu)
        choice = input("[1/2]>>>:")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                if self.active_hosts():
                    file_name = input("Input File Name/Dir Name:")
                    local_file_path = os.path.join(settings.FILE_DIR, file_name)
                    if os.path.isfile(local_file_path) or os.path.isdir(local_file_path):
                        remote_file_path = input("Input Remote Path:")
                    else:
                        return print("\033[31;1mFile/Dir is not exists\033[0m")
                    thread_list = []
                    for host in self.host_obj_list:
                        t = threading.Thread(target=host.sftp_put_file, args=(local_file_path,remote_file_path))
                        t.setDaemon(True)
                        thread_list.append(t)
                        t.start()
                        self.logger.info("%s put file(%s) to (%s)" % (host.name, local_file_path, remote_file_path))
                    for t in thread_list:
                        t.join()
            elif choice == 2:
                if self.active_group():
                    file_name = input("Input File Name/Dir Name:")
                    if os.path.isfile(file_name) or os.path.isdir(file_name):
                        local_file_path = os.path.join(settings.FILE_DIR,file_name)
                        remote_file_path = input("Input Remote Path:")
                    else:
                        return print("\033[31;1mFile/Dir is not exists\033[0m")
                    thread_list = []
                    for group in self.group_obj_list:
                        print("Group:%s".center(50, "=") % group.name)
                        for host in group.hosts_list:
                            t = threading.Thread(target=host.sftp_put_file, args=(local_file_path,remote_file_path))
                            t.setDaemon(True)
                            thread_list.append(t)
                            t.start()
                            self.logger.info("%s put file(%s) to (%s)" % (host.name, local_file_path, remote_file_path))
                    for t in thread_list:
                        t.join()
            else:
                print("\033[31;1mWrong Number\033[0m")
        else:
            print("\033[31;1mChoice must a Number...\033[0m")

    def get_file(self):
        '''

        '''
        menu = '''
                        1. Choose Host[s]
                        2. Choose Group
                        '''
        print(menu)
        choice = input("[1/2]>>>:")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                if self.active_hosts():
                    remote_file_path = input("Input File Name/Dir Name:")
                    thread_list = []
                    for host in self.host_obj_list:
                        t = threading.Thread(target=host.sftp_get_file, args=(remote_file_path,))
                        t.setDaemon(True)
                        thread_list.append(t)
                        t.start()
                        self.logger.info("get file(%s) from (%s)" % (remote_file_path, host.name))
                    for t in thread_list:
                        t.join()
            elif choice == 2:
                if self.active_group():
                    remote_file_path = input("Input File Name/Dir Name:")
                    thread_list = []
                    for group in self.group_obj_list:
                        print("Group:%s".center(50, "=") % group.name)
                        for host in group.hosts_list:
                            t = threading.Thread(target=host.sftp_get_file, args=(remote_file_path,))
                            t.setDaemon(True)
                            thread_list.append(t)
                            t.start()
                            self.logger.info("get file(%s) from (%s)" % (remote_file_path,host.name))
                    for t in thread_list:
                        t.join()
            else:
                print("\033[31;1mWrong Number\033[0m")
        else:
            print("\033[31;1mChoice must a Number...\033[0m")

    def add_host(self):
        '''
        新建主机
        输入参数:name,ip,port,username,password,group_obj
        '''
        name = input("Input the host NAME:")
        #判断主机是否存在
        host_dic = self.print_list(out_put=False)
        if host_dic.get(name):
            return print("\033[31;1mHost exists,Add Failed...\033[0m")
        ip = input("Input the host IP:")
        # 判断IP规范
        if not re.fullmatch('(\d{1,3}\.){1,3}\d{1,3}', ip):
            return print("\033[31;1mWrong IP,Add Failed...\033[0m")
        port = input("Input the host PORT:")
        #判断端口
        if not (0 < int(port) < 65535):
            return print("\033[31;1mWrong port,Add Failed...\033[0m")
        username = input("Input the connect USERNAME :")
        password = input("Input the host PASSWORD:")
        group_dic = self.print_group()
        group_name = input("Input the host GROUP:")
        #判断组输入
        if group_dic.get(group_name):
            group_obj = group_dic.get(group_name)
        else:
            return print("\033[31;1mWrong groups,Add Failed...\033[0m")
        #执行新建,传入参数
        host_obj = basic.Host(name,ip,int(port),username,password,group_name)
        res1 = host_obj.add_new()
        #把主机对象加入属组
        res2 = group_obj.add_host(host_obj)
        if res1 and res2:
            self.logger.info("Add New Host:%s:%s(%s:%s):" % (host_obj.name,host_obj.group,host_obj.ip,host_obj.port))
            return print("\033[32;1mHost is added...\033[0m")

    def add_group(self):
        '''
        新建组
        输入参数:group_name
        '''
        groupname = input("Input the GROUP_NAME:")
        group_dic = self.print_group(out_put=False)
        #判断组是否存在
        if group_dic.get(groupname):
            return print("\033[31;1mGroup exists,Add Failed...\033[0m")
        group = basic.Group(groupname)
        res = group.add_new()
        if res:
            self.logger.info("Add New Group %s" % groupname)
            return print("\033[32;1mGroup is added...\033[0m")

    def change_host(self):
        '''
        修改主机的参数
        [name][ip][port][username][password][groups]
        '''
        host_dic = self.print_list()
        host = input("Input the host name(you want change):")
        if not host_dic.get(host):
            return print("Wrong name...")
        host_obj = host_dic.get(host)
        choice = input("Which detail you want change?[name][ip][port][username][password][group]?")
        if choice == "group":
            group_dic = self.print_group()
            group_name = input("Input the new GROUP:")
            # 判断组输入
            if group_dic.get(group_name):
                if group_name == host_obj.group:
                    return print("\033[31;1m%s is %s group now...\033[0m" % (host_obj.name,group_name))
                group_obj = group_dic.get(group_name)
                old_group_obj = group_dic.get(host_obj.group)
            else:
                return print("\033[31;1mWrong groups,Change Failed...\033[0m")
            # 将主机从原有属组中删除
            res1 = old_group_obj.remove_host(host_obj)
            # 将主机的属组更改为新属组
            res2 = group_obj.add_host(host_obj)
            # 将主机添加到新属组
            host_obj.group = group_name
            res3 = host_obj.update()
            # print("res",res1,res2,res3)
            if res1 and res2 and res3:
                self.logger.info("Host:%s's group from %s change to %s" % (host_obj.name,old_group_obj.name,group_obj.name) )
                return print("\033[32;1mChange success...\033[0m")
            else:
                return False
        attr = host_obj.change_attr(choice)
        if attr:
            self.logger.info("Host:%s's %s from %s change to %s" % (host_obj.name,choice,getattr(host_obj,choice),attr))
            print("\033[32;1mChange success...\033[0m")
        else:
            return print("\033[31;1mWrong input...\033[0m")
