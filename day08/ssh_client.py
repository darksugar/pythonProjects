#Authon Ivor
import socket

client = socket.socket()
client.connect(('localhost',9999))

while True:
    choice = input(">>>:")
    client.send(choice.encode())
    res = client.recv(1024)
    print(res.decode())

