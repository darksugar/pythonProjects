#Authon Ivor

import socket

s = socket.socket()
s.bind(('localhost',9999))
s.listen(5)

while True:
    conn,client_addr = s.accept()
    print("Got a new conn",conn)
    while True:
        data = conn.recv(1024)
        print("recv data:",data)
