#Author:Ivor
import os,sys,time
import socket
HOST,PORT = 'localhost',9999
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

while True:
    print("等待连接……")
    conn,addr = s.accept()
    print("有终端连入,",conn)
    while True:
        recv = conn.recv(1024)
        res = os.popen(str(recv.decode())).read()
        conn.send(res.encode())
