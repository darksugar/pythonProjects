#Authon Ivor
import redis

c = redis.Redis('localhost',6379,0)

c.set('name','ivor')

name = c.get('name')
print(name)