#Authon Ivor

import json
info = {
    "name":"Ivor",
    "age":"27",
}

with open("jsondump.json","r") as f:
    a = json.loads(f.read())

with open("jsondump.json","r") as f:
    b = json.load(f)

print(a,b)