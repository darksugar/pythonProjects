#Authon Ivor
import socket
import selectors
import json

class FTP_Server(object):
    def __init__(self):
        self.server = self.initialize()
        self.select = selectors.DefaultSelector()
        self.select.register(self.server, selectors.EVENT_READ, self.accept)

    def initialize(self):
        HOST, PORT = 'localhost', 9999
        server = socket.socket()
        server.bind((HOST, PORT))
        server.listen(50)
        server.setblocking(False)
        return server

    def start_serve(self):
        while True:
            event = self.select.select()
            for key, mask in event:
                callback = key.data
                callback(key.fileobj, mask)

    def accept(self,sock,mask):
        conn, addr = sock.accept()
        print("New connection",addr)
        conn.setblocking(False)
        self.select.register(conn,selectors.EVENT_READ,self.interactive)

    def interactive(self,conn,mask):
        res = conn.recv(1024)
        data = json.loads(res.decode())
        if not data:conn.close()
        if data.get("action"):
            if hasattr(self, "_%s" % data.get("action")):
                func = getattr(self,"_%s" % data.get("action"))
                func(conn,data)

    def _echo(self,conn,data):
        conn.send(data.get("msg").encode())

    def _put(self):
        pass
    def _get(self):
        pass

if __name__ == '__main__':
    server = FTP_Server()
    server.start_serve()