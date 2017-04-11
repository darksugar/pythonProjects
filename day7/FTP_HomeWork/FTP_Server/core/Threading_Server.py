#Authon Ivor
import socketserver
import json
import configparser
import os,sys
import subprocess
import hashlib
from conf import settings
STATUS_CODE = {
    250: "Invalid cmd format,e.g:{'action':'get','filename':'test.py','size':344",
    251: "Invalid cmd",
    252: "Invalid auth data",
    253: "Incorrect username or password",
    254: "Passed auth",
    255: "Starting send file",
    256: "File is not exists",
    257: "MD5 verifycation",
    258: "dir result",
    259: "Ready to receive file",
    260: "Receive complete",
    261: "Dir is not exist",
    262: "Dir change success",
    263: "Dir is exist",
    264: "Dir created success",
    265: "free space is not enough"
    }
class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if len(self.data) == 0:
                print("Client is close")
                break
            print("client_address---",self.client_address)
            print("client_data---",self.data)
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                if hasattr(self,"_%s" % data.get('action')):
                    func = getattr(self,"_%s" % data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code': status_code, 'status_msg': STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode('utf-8'))

    def _auth(self,*args,**kwargs):
        data = args[0]
        if data.get("username") and data.get("password"):
            user = self.authenticate(data.get("username"),data.get("password"))
            print("user---",user)
            if user:
                print("Passed authentication",user)
                self.user = user
                self.send_response(254)
            else:
                self.send_response(253)
        else:
            self.send_response(252)

    def authenticate(self,username,password):
        '''验证用户合法性，和法则返回用户数据'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            print(config[username]["Password"])
            if _password == password:
                config[username]["Username"] = username
                return config[username]

    def get_free_size(self,user):
        root_dir = "%s/%s" % (settings.USER_HOME, user)
        total_size = 0
        for dir,c_dir,files in os.walk(root_dir):
            for file in files:
                size = os.path.getsize(os.path.join(dir,file))
                total_size += size
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        quotation = config[user]["Quotation"]
        quotation = int(quotation.replace("M",""))
        quotation = quotation*1024*1024
        return quotation - total_size

    def _get(self,*args,**kwargs):
        recv_data = args[0]
        print("get_recv_data----",recv_data)
        if recv_data.get('action') == 'get':
            user_home_dir = '%s/%s' % (settings.USER_HOME, self.user['Username'])
            file_abs_name = '%s/%s' % (user_home_dir, recv_data.get('file_name'))
            print("get_file_abs_name---",file_abs_name)
            if os.path.isfile(file_abs_name):
                file_size = os.path.getsize(file_abs_name)
                response_data = {"file_size":file_size}
                self.send_response(255,response_data)
                self.request.recv(1)#防止粘包
                file_obj = open(file_abs_name,'rb')
                if recv_data.get("md5"):
                    md5_obj = hashlib.md5()
                    for line in file_obj:
                        self.request.send(line)
                        md5_obj.update(line)
                    else:
                        md5_var = md5_obj.hexdigest()
                        self.send_response(257,data={"md5_hexdigest":md5_var})
                else:
                    for line in file_obj:
                        self.request.send(line)
                file_obj.close()
            else:
                self.send_response(256)
        else:
            self.send_response(250)

    def _put(self,*args,**kwargs):
        recv_data = args[0]
        if recv_data.get("action") == "put":
            file_name = recv_data.get("file_name")
            file_abs_name = os.path.join(os.path.join(settings.USER_HOME, recv_data.get("path")),file_name)
            file_size = recv_data.get("file_size")
            free_size = self.get_free_size(recv_data.get("user"))
            print("Free_size---",free_size)
            print("File_size---",file_size)
            if  file_size > free_size:
                self.send_response(265)
                return
            self.send_response(259)
            file_obj = open(file_abs_name,'wb')
            receive_size = 0
            if recv_data.get("md5"):
                md5_obj = hashlib.md5()
                while receive_size < file_size:
                    recv =self.request.recv(4096)
                    file_obj.write(recv)
                    md5_obj.update(recv)
                    receive_size += len(recv)
                else:
                    md5_var = md5_obj.hexdigest()
                    self.send_response(257,data={"md5_hexdigest":md5_var})
            else:
                while receive_size < file_size:
                    recv =self.request.recv(4096)
                    file_obj.write(recv)
                    receive_size += len(recv)
                else:
                    self.send_response(260)
        else:
            self.send_response(250)

    def _ls(self,*args,**kwargs):
        data = args[0]
        if data.get("action") == 'ls':
            if data.get("path"):
                current_dir = os.path.join(settings.USER_HOME,data.get("path"))
                print(settings.USER_HOME,data.get("path"))
                print("ls_current_dir---",current_dir)
                sub_obj = subprocess.Popen('ls',cwd=current_dir,shell=True,stdout=subprocess.PIPE)
                dir_res = sub_obj.stdout.read().decode()
                if dir_res:
                    self.send_response(258,data={"dir_res":dir_res})
                else:
                    self.send_response(251)
        else:
            self.send_response(251)

    def _dir(self,*args,**kwargs):
        data = args[0]
        if data.get("action") == 'dir':
            if data.get("path"):
                current_dir = os.path.join(settings.USER_HOME,data.get("path"))
                print(settings.USER_HOME,data.get("path"))
                print("ls_current_dir---",current_dir)
                sub_obj = subprocess.Popen('dir',cwd=current_dir,shell=True,stdout=subprocess.PIPE)
                dir_res = sub_obj.stdout.read().decode("GBK")
                if dir_res:
                    self.send_response(258,data={"dir_res":dir_res})
                else:
                    self.send_response(251)
        else:
            self.send_response(251)

    def _cd(self,*args,**kwargs):
        data = args[0]
        if data.get('action') == 'cd':
            if data.get('path'):
                chg_dir = os.path.join(settings.USER_HOME,data.get('path'))
                print("chg_dir---",chg_dir)
                if os.path.isdir(chg_dir):
                    self.send_response(262)
                else:
                    self.send_response(261)

    def _mkdir(self,*args,**kwargs):
        data = args[0]
        if data.get("action") == 'mkdir':
            if data.get("dir_name"):
                dir_name = os.path.join(settings.USER_HOME,data.get("dir_name"))
                if os.path.isdir(dir_name):
                    self.send_response(263)
                else:
                    os.mkdir(dir_name)
                    print("mkdir---",dir_name)
                    self.send_response(264)