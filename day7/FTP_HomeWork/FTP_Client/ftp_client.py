# -*-coding=utf-8-*-
import socket
import json
import optparse
import hashlib
__author__ = 'Ivor'


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="FTP server ip addr")
        parser.add_option("-p", "--port", type='int', dest="port", help="FTP server ip port")
        parser.add_option("-u", "--username", dest="username", help="user")
        parser.add_option("-P", "--password", dest="password", help="password")
        self.option, self.args = parser.parse_args()
        self.verify_args()
        self.make_connection()

    def verify_args(self):
        '''验证参数合法性'''
        if self.option.server and self.option.port:
            print(self.option)
            if self.option.port > 0 and self.option.port < 65535:
                return True
            else:
                exit("Port must be in 0 - 65535..")
        else:
            exit("Server or Port args missing..")

    def make_connection(self):
        '''连接服务端'''
        self.sock = socket.socket()
        self.sock.connect((self.option.server, self.option.port))

    def authenticate(self):
        '''用户验证'''
        if self.option.username:
            print(self.option.username, self.option.password)
            return self.get_auth_result(self.option.username, self.option.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password:").strip()
                if self.get_auth_result(username, password):
                    return True
                retry_count += 1

    def get_auth_result(self, username, password):
        '''获取服务端回复'''
        data = {
            "action": "auth",
            "username": username,
            "password": password
        }
        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print("Passed authentication!")
            self.user = username
            self.path = "/%s" % self.user
            return True
        else:
            print(response.get('status_msg'))

    def get_response(self):
        '''处理服务器回复结果'''
        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        return data

    def interactive(self):
        '''开始交互'''
        if self.authenticate():
            print("-----start interactive-----")
            while True:
                choice = input("[%s][%s]>>>:" % (self.user,self.path)).strip()
                if len(choice) == 0: continue
                cmd_list = choice.split()
                if hasattr(self ,"_%s" % cmd_list[0]):
                    func = getattr(self, "_%s" % cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")
        else:
            exit("something wrong")

    def md5_check(self,cmd_list):
        '''md5检测'''
        if '--md5' in cmd_list:
            return True

    def show_progess(self,total):
        receive_size = 0
        current_percent = 0
        while receive_size < total:
            if int((receive_size / total) * 100)  > current_percent :
                print("#",end='',flush=True)
                current_percent += 10
            new_size = yield
            receive_size += new_size

    def _get(self, cmd_list):
        print("get", cmd_list[0],cmd_list[-1])
        if len(cmd_list) < 2:return print("Need a filename")
        header = {
            "action": "get",
            "file_name": cmd_list[1]
        }
        if self.md5_check(cmd_list):
            header.update({"md5":True})
        self.sock.send(json.dumps(header).encode("utf-8"))
        response = self.get_response()
        self.sock.send(b'1') #防止粘包
        if response.get('status_code') == 255:
            print("start download")
            receive_size = 0
            file_size = response.get("file_size")
            file_name = cmd_list[1]
            file_obj = open(file_name, 'wb')
            process = self.show_progess(file_size)
            process.__next__()
            if self.md5_check(cmd_list):
                md5_obj = hashlib.md5()
                while receive_size < file_size:
                    recv = self.sock.recv(4096)
                    try:
                        process.send(len(recv))
                    except StopIteration:
                        print("100%")
                    file_obj.write(recv)
                    receive_size += len(recv)
                    md5_obj.update(recv)
                else:
                    md5_var = md5_obj.hexdigest()
                    end_response = self.get_response()
                    print(end_response.get("md5_hexdigest"),md5_var)
                    if end_response.get("md5_hexdigest") == md5_var:
                        print("文件一致性校验成功！")
                    else:
                        print("文件校验出错！")
            else:
                while receive_size < file_size:
                    recv = self.sock.recv(4096)
                    try:
                        process.send(len(recv))
                    except StopIteration:
                        print("100%")
                    file_obj.write(recv)
                    receive_size += len(recv)
            file_obj.close()
        else:
            print(response.get('status_msg'))

    def _ls(self, cmd_list):
        if len(cmd_list) > 1:
            return print("Invalid argv.")
        data = {
            "action": "ls",
            "path":self.path
        }
        self.sock.send(json.dumps(data).encode("utf-8"))
        response = self.get_response()
        if response.get("status_code") == 258:
            dir_res = response.get("dir_res")
            print(dir_res)
        else:
            print(response.get('status_msg'))


if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()