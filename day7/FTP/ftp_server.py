#Authon Ivor
import socket
import json
import os

ip = ('localhost',9999)
s = socket.socket()
s.bind(ip)
s.listen(5)

while True:
    print("等待连接中....")
    conn,client_addr = s.accept()
    print("有用户主动接入:", conn, client_addr)
    while True:
        data = conn.recv(4096)
        data = json.loads(data.decode('utf-8'))
        if data.get('action') is not None:
            if data['action'] == 'put':
                file_obj = open(data['file_name'],'wb')
                receive_size = 0
                file_size = data['file_size']
                while receive_size < file_size:
                    recv = conn.recv(4096)
                    file_obj.write(recv)
                    receive_size += len(recv)
                    print(file_size,receive_size)
                file_obj.close()
                print("File receive complete!")
            elif data['action'] == 'get':
                pass