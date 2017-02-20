__author__ = "Ivor"

user,passwd = "ivor","abc"

def authtication(auth_type):
    def auth_type_select(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Please input your username:")
                password = input("Please input your password:")
                if username == user and password == passwd:
                    print("authtication successed!")
                    func(*args, **kwargs)
                else:
                    exit("failed!")
            elif auth_type == "ldap":
                print("ldap")

        return wrapper
    return auth_type_select

def index():
    print("this is index!")
@authtication(auth_type = "local")
def home(name):
    print("this is home!")
    print("Hi,%s" % name )

@authtication(auth_type = "ldap")
def bbs():
    print("this is bbs!")

index()
home("haha")
bbs()