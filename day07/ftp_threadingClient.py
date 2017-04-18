#Authon Ivor
import os
import json
import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    choice = input(">>>:")
    if len(choice) == 0:continue
    client.send(choice.encode('utf-8'))
    data =client.recv(1024)
    print(data)