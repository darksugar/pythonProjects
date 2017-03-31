#Authon Ivor
__Author__ = 'Ivor'


import socket


client = socket.socket()
client.connect(('localhost',9999))

client.send(b"Hello World!")

data = client.recv(1024)
print(data)
client.close()