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
@authtication(auth_type = "local") #bbs = authtication(auth_type="ldap")(home("dark"))
def home(name):
    print("this is home!")
    print("Hi,%s" % name )


@authtication(auth_type = "ldap")
def bbs():
    print("this is bbs!")


index()
home("haha")
bbs()

#!/usr/bin/env python

#coding:utf-8


def Before(request,kargs):

    print('before')


def After(request,kargs):

    print('after')


def Filter(before_func,after_func):

    def outer(main_func):

        def wrapper(request,kargs):

            before_result = before_func(request,kargs)

            if(before_result != None):

                return before_result

            main_result = main_func(request,kargs)

            if(main_result != None):

                return main_result

            after_result = after_func(request,kargs)

            if(after_result != None):

                return after_result

        return wrapper

    return outer


@Filter(Before, After)

def Index(request,kargs):

    print('index')