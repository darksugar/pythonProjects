#Authon Ivor
import socket

ip = ('localhost',9999)
server = socket.socket()
server.bind(ip)

server.listen()
print("我要开始等电话了")

#conn就是客户端连接过来，在服务端生成的连接实例
conn,addr = server.accept()
print("电话来了")
print(conn,addr)

data = conn.recv(1024)
conn.send(data.upper())
server.close()