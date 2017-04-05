#Authon Ivor
import socket
import os,sys
import json
import optparse

class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="FTP server ip addr")
        parser.add_option("-p","--port",type='int',dest="port",help="FTP server ip port")
        parser.add_option("-u","--username",dest="username",help="user")
        parser.add_option("-P","--password",dest="password",help="password")
        self.option , self.args = parser.parse_args()
        self.verify_args(self.option,self.args)
        self.make_connection()
    def verify_args(self,option,args):
        '''验证参数合法性'''
        if option.server and option.port:
            print(option)
            if option.port > 0 and option.port < 65535:
                return True
            else:
                exit("Port must be in 0 - 65535..")
    def make_connection(self):
        '''连接服务端'''
        self.sock = socket.socket()
        self.sock.connect((self.option.server,self.option.port))
    def authenticate(self):
        '''用户验证'''
        if self.option.username:
            print(self.option.username,self.option.password)
            return self.get_auth_result(self.option.username,self.option.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password:").strip()
                return  self.get_auth_result(username,password)
    def get_auth_result(self,username,password):
        '''获取服务端回复'''
        data = {
            "action":"auth",
            "username":username,
            "password":password
        }
        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print("Passed authentication!")
            self.user = username
            return True
        else:
            print(response.get('status_msg'))
    def get_response(self):
        '''处理服务器回复结果'''
        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        return data
    def interactive(self):
        if self.authenticate():
            print("-----start interactive-----")
            while True:
                choice = input("[%s]>>>:" % self.user).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
                if hasattr(self,"_%s" % cmd_list[0]):
                    func = getattr(self,"_%s" % cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")
        else:
            exit("something wrong")
    def _get(self,cmd_list):
        print("get",cmd_list)
if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()