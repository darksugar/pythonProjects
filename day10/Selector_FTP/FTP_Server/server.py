#Authon Ivor
import socket
import selectors
import json
import pickle
import os
STATUS_CODE = {
    200: "Ready to receive file",
    201: "Ready to send file",
    301: "File not exists"
    }
class FTP_Server(object):
    def __init__(self):
        self.server = self.initialize()
        self.select = selectors.DefaultSelector()
        self.select.register(self.server, selectors.EVENT_READ, self.accept)

    def initialize(self):
        HOST, PORT = 'localhost', 9999
        server = socket.socket()
        server.bind((HOST, PORT))
        server.listen(50)
        server.setblocking(False)
        return server

    def start_serve(self):
        while True:
            event = self.select.select()
            for key, mask in event:
                callback = key.data
                callback(key.fileobj,mask)

    def accept(self,conn,mask):
        conn, addr = conn.accept()
        print("New connection",addr)
        conn.setblocking(False)
        self.select.register(conn,selectors.EVENT_READ,self.interactive)

    def interactive(self,conn,mask):
        res = conn.recv(4096)
        # print("res",res)
        data = pickle.loads(res)
        # print("data,",type(data),data)
        if not data:conn.close()
        if data.get("action"):
            if hasattr(self, "_%s" % data.get("action")):
                    func = getattr(self,"_%s" % data.get("action"))
                    func(conn,data)

    def _put(self,conn,*args,**kwargs):
        recv_data = args[0]
        file_name = recv_data.get("file_name")
        file_size = recv_data.get("file_size")
        if os.path.isfile(file_name):
            file_obj = open(file_name, 'ab')
        else:
            file_obj = open(file_name, 'wb')
        if recv_data.get("detail") == "put_file":
            conn.send(b"y")
            recv = recv_data.get("line")
            file_obj.write(recv)
            if os.path.getsize(file_name) == file_size:
                file_obj.close()
                print("get done")
        else:
            self.send_response(conn,200)
            print("send 200 done")
            print(recv_data)

    def _get(self,conn,*args,**kwargs):
        recv = args[0]
        file_name = recv.get("file_name")
        if os.path.isfile(file_name):
            file_size = os.path.getsize(file_name)
            self.send_response(conn,201,{"file_size":file_size})
            file_obj = open(file_name,"rb")
            for data in file_obj:
                conn.send(data)
            else:
                print("send done")
        else:
            self.send_response(conn,301)

    def send_response(self,conn, status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code': status_code, 'status_msg': STATUS_CODE[status_code]}
        if data:
            response.update(data)
        conn.send(json.dumps(response).encode('utf-8'))



if __name__ == '__main__':
    server = FTP_Server()
    server.start_serve()