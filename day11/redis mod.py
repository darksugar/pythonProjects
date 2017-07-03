#Authon Ivor
import redis

c = redis.Redis(host='192.168.116.131',port=6379,db=0)

c.set('name','ivor')

name = c.get('name')
print(name)
