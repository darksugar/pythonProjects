#Authon Ivor
import socketserver
import json
import configparser
from conf import settings
STATUS_CODE = {
    250:"Invalid cmd format,e.g:{'action':'get','filename':'test.py','size':344",
    251:"Invalid cmd ,e.g:{'action':'get','filename':'test.py','size':344",
    252:"Invalid auth data",
    253:"Incorrect username or password",
    254:"Passed auth",
              }
class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if len(self.data) == 0:
                print("Client is close")
                break
            print(self.client_address)
            print(self.data)
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                if hasattr(self,"_%s" % data.get('action')):
                    func = getattr(self,"_%s" % data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)
    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode('utf-8'))
    def _auth(self,*args,**kwargs):
        data = args[0]
        if data.get("username") and data.get("password"):
            user = self.authenticate(data.get("username"),data.get("password"))
            print("user---",user)
            if user:
                print("Passed authentication",user)
                self.send_response(254)
            else:
                self.send_response(253)
        else:
            self.send_response(252)
    def authenticate(self,username,password):
        '''验证用户合法性，和法则返回用户数据'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            print(config[username]["Password"])
            if _password == password:
                return config[username]
            else:
                return False
    def _get(self,*args,**kwargs):
        pass
    def _put(self,*args,**kwargs):
        pass
    def _cd(self,*args,**kwargs):
        pass
    def _ls(self,*args,**kwargs):
        pass