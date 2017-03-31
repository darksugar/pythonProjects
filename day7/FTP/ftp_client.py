#Authon Ivor
import os
import socket
import json

client = socket.socket()
client.connect(('localhost',9999))

while True:
    choice = input(">>>:")
    if len(choice) == 0:continue
    cmd_list = choice.split()
    if cmd_list[0] == 'put':
        if len(cmd_list) == 1:
            print("Need a filename... ")
            continue
        filename = cmd_list[1]
        if os.path.isfile(filename):
            file_obj = open(filename,'rb')
            base_filename = filename.split("/")[-1]
            file_size = os.path.getsize(filename)
            print(base_filename,file_size)
            data_header = {
                "action":"put",
                "filename":base_filename,
                "size":file_size
            }
            client.send( json.dumps(data_header).encode('utf-8') )
        else:
            print("File is not exist.")
    elif cmd_list[0] == 'get':
        pass