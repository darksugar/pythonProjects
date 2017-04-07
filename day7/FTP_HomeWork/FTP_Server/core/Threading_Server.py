#Authon Ivor
import socketserver
import json
import configparser
import os,sys
import subprocess
import hashlib
from conf import settings
STATUS_CODE = {
    250:"Invalid cmd format,e.g:{'action':'get','filename':'test.py','size':344",
    251:"Invalid cmd ,e.g:{'action':'get','filename':'test.py','size':344",
    252:"Invalid auth data",
    253:"Incorrect username or password",
    254:"Passed auth",
    255:"Starting send file",
    256:"File is not exists",
    257:"MD5 verifycation",
    258:"dir result",
    259:"Ready to receive file",
    260:"Receive complete"

              }
class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if len(self.data) == 0:
                print("Client is close")
                break
            print(self.client_address)
            print(self.data)
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

    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
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

    def _get(self,*args,**kwargs):
        recv_data = args[0]
        print(recv_data)
        if recv_data.get('action') == 'get':
            user_home_dir = '%s/%s' % (settings.USER_HOME, self.user['Username'])
            file_abs_name = '%s/%s' % (user_home_dir, recv_data.get('file_name'))
            print(file_abs_name)
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
            self.send_response(259)
            file_name = recv_data.get("file_name")
            file_abs_name = os.path.join(os.path.join(settings.USER_HOME, recv_data.get("path")),file_name)
            file_size = recv_data.get("file_size")
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

    def _cd(self,*args,**kwargs):
        pass
    def _ls(self,*args,**kwargs):
        data = args[0]
        if data.get("action") == 'ls':
            if data.get("path"):
                current_dir = os.path.join(settings.USER_HOME,data.get("path"))
                print(settings.USER_HOME,data.get("path"))
                print(current_dir)
                sub_obj = subprocess.Popen('dir',cwd=current_dir,shell=True,stdout=subprocess.PIPE)
                dir_res = sub_obj.stdout.read().decode("GBK")
                self.send_response(258,data={"dir_res":dir_res})
        else:
            self.send_response(251)



