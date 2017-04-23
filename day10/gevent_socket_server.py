# -*- coding:utf-8 -*-
__Author__ = 'Ivor'
import socket
import gevent
from gevent import monkey,socket

monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(("localhost",port))
    s.listen(500)
    # conn,addr = s.accept()
    # handler(conn)
    while True:
        conn,addr = s.accept()
        gevent.spawn(handler,conn)

def handler(conn):
    try:
        while True:
            data = conn.recv(1024)
            conn.send(data.upper())
    except Exception as e:
        print("Exception",e)


if __name__ == '__main__':
    server(8001)
