#Authon Ivor
import os
import json
import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    choice = input(">>>:")
    if len(choice) == 0:continue
    cmd_list = choice.split()
    if cmd_list[0] == 'put':
        if cmd_list[-1]:
            file_name = cmd_list[-1]
            if os.path.isfile(file_name):
                base_filename = file_name.split("/")[-1]
                file_size = os.path.getsize(file_name)
                file_obj = open(file_name,'rb')
                data_header = {
                    "action":"put",
                    "file_name":base_filename,
                    "file_size":file_size
                }
                client.send(json.dumps(data_header).encode('utf-8'))
                for line in file_obj:
                    client.send(line)
                print("File send complete.".center(50,'-'))
            else:
                print("File is not exists.")
        else:
            print("Need a file...")
    elif cmd_list[0] == 'get':
        pass
    else:
        print("Wrong input.")