#Authon Ivor
import socket
import json,os,time
import pickle

class FTP_Client(object):
    def __init__(self):
        HOST, PORT = 'localhost', 9999
        self.client = socket.socket()
        self.client.connect((HOST, PORT))
        self.interactiver()

    def interactiver(self):
        while True:
            cmd = input(">>>:")
            if len(cmd) == 0: continue
            cmd_list = cmd.split()
            if hasattr(self, "_%s" % cmd_list[0]):
                func = getattr(self, "_%s" % cmd_list[0])
                func(cmd_list)
            else:
                print("Invalid cmd.")

    def get_response(self):
        '''处理服务器回复结果'''
        data = self.client.recv(1024)
        data = json.loads(data.decode())
        return data

    def send_data(self, data):
        '''发送头文件，请求交互'''
        send_data = pickle.dumps(data)
        self.client.sendall(send_data)

    def show_progress(self,total):
        receive_size = 0
        current_percent = 0
        while receive_size < total:
            if int((receive_size / total) * 100)  > current_percent :
                print("#",end='',flush=True)
                current_percent += int((receive_size / total) * 100)
            receive_size += yield

    def _put(self, cmd_list):
        if len(cmd_list) < 2: return print("Need a filename")
        if os.path.isfile(cmd_list[1]):
            file_name = cmd_list[1]
            file_size = os.path.getsize(file_name)
            header = {
                "action":"put",
                "file_name":file_name,
                "file_size":file_size
            }
            self.send_data(header)
            response = self.get_response()
            file_obj = open(file_name, 'rb')
            file_obj.seek(0)
            if response.get("status_code") == 200:
                print("starting send file")
                progress = self.show_progress(file_size)
                progress.__next__()
                while True:
                    # data = file_obj.read(947)
                    # if len(data)==0:break
                    for data in file_obj:
                        file = {
                            "action":"put",
                            "file_name": file_name,
                            "file_size": file_size,
                            "detail":"put_file",
                            "line":data
                        }
                        self.send_data(file)
                        self.client.recv(1)
                        try:
                            progress.send(len(data))
                            # print(len(line))
                        except:
                            print("100%")
                else:
                    print("File send done")
            else:
                self.get_response()
            file_obj.close()
            print("send success")
            if response.get("status_code") == 300:
                print(response.get("status_msg"))
        else:
            print("File is not exist")

    def _get(self, cmd_list):
        if len(cmd_list) < 2: return print("Need a filename")
        file_name = cmd_list[1]
        header = {
            "action":"get",
            "file_name":file_name
        }
        self.send_data(header)
        response = self.get_response()
        if response.get("status_code") == 201:
            file_obj = open(file_name,"wb")
            current_size = 0
            while current_size < response.get("file_size"):
                recv = self.client.recv(4096)
                file_obj.write(recv)
                current_size += len(recv)
        else:
            print(response.get("status_msg"))

if __name__ == '__main__':
    client = FTP_Client()