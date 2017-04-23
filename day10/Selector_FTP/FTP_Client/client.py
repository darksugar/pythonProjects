#Authon Ivor
import socket
import json
# HOST,PORT = 'localhost',10000
HOST,PORT = 'localhost',9999
client = socket.socket()
client.connect((HOST,PORT))
while True:
    msg = input(">>>:")
    if len(msg)==0:continue
    header = {
        "action":msg,
        "msg":"mmmsg"
    }
    client.send(json.dumps(header).encode())
    data = client.recv(1024)
    print(data)