#Authon Ivor
import optparse
import socketserver
from conf import settings
from core.Threading_Server import FTPHandler

class ArgsHandler():
    def __init__(self):
        self.parser = optparse.OptionParser()
        # self.parser.add_option("-s",'--server',dest='server',help='The server address')
        # self.parser.add_option('-p','--port',dest='port',help='The server port')
        (self.option , self.args) = self.parser.parse_args()
        self.verify_args(self.option,self.args)
    def verify_args(self,option,args):
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.parser.print_help()
    def start(self):
        print('start'.center(30,'-'))
        server = socketserver.TCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()

