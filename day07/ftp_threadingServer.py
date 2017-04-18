#Authon Ivor
import socketserver

class MyHandelclass(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(4096)
            print(self.client_address)
            print(self.data)
            self.request.sendall(self.data.upper())

if  __name__ == '__main__':
   server = socketserver.ThreadingTCPServer(('localhost',9999),MyHandelclass)
   server.serve_forever()