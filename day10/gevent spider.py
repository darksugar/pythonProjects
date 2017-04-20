#Authon Ivor
from gevent import monkey
from urllib import request
import gevent
import time

monkey.patch_all() #把当前程序都的所有io操作单独加上标记

urls = [
        'https://www.yahoo.com',
        'https://www.python.org',
        'https://github.com'
]
def get(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    with open("url.html","wb") as f:
        f.write(data)
start_time = time.time()
for url in urls:
    get(url)
print("同步cost time ,",time.time() - start_time)

async_time = time.time()
gevent.joinall(
    [gevent.spawn(get,'https://www.yahoo.com'),
     gevent.spawn(get,'https://www.python.org'),
     gevent.spawn(get,'https://github.com'),
     ]
)
print("异步cost time,",time.time() - async_time)
