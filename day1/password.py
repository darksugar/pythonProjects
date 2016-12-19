#Author:Ivor
import getpass
_username = "Ivor"
_password = "abc123"
username = input("username:")
password = input("password:")
#password = getpass.getpass("password:")

if username == _username and password == _password:
    print("Welcome user {name}".format(name=_username))
else:
    print("Invalid username or password!")

