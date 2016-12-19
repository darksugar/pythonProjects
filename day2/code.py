#Author:Ivor

msg='天安门'

print(msg.encode(encoding='gb2312'))

mss=b'\xcc\xec\xb0\xb2\xc3\xc5'

print(mss.decode(encoding='GBK'))

