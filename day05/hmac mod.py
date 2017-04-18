#Authon Ivor

import hmac

name = "天气不错".encode(encoding="utf-8")
print(name)
h_obj = hmac.new(b"Salt",name)
print(h_obj.hexdigest())
