#Authon Ivor

import json
# info = {
#     "name":"Ivor",
#     "age":"27",
#}

info = ["a","b","c","f","f","g"]
with open("jsondump.json","w") as f:
    f.write(json.dumps(info))

with open("jsondump.json","w") as f:
    json.dump(info,f)
