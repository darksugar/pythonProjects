#Authon Ivor
import requests,json,time,datetime
#登陆url
url1 = 'http://cre.huoyunren.com/inside.php?t=json&m=login&f=getallcode&opurl=/login/index.html'
#车辆使用情况
url2 = 'http://cre.huoyunren.com/inside.php?t=json&m=statistics&f=truckuse&opurl=/statistics/truckuse.html'
#车辆油耗情况
url3 = 'http://cre.huoyunren.com/inside.php?t=json&m=fuel&f=fuelmonthlist&opurl=/fuelreport/fuelmonthlist.html'
#登陆用头文件
headers = {'Accept':'*/*',
           'Accept-Encoding':'gzip,deflate',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'Connection':'keep-alive',
           'Content-Length':'75',
           'Content-Type':'application/x-www-form-urlencoded',
           'Host':'cre.huoyunren.com',
           'Origin':'http://cre.huoyunren.com',
           'Referer':'http://cre.huoyunren.com/login/index.html',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
           'X-Requested-With':'XMLHttpRequest'}
#登陆用post数据
data = {'username':'bjysb',
        'password':'123456',
        'checkcode':'',
        'loginflag':'1',
        'cookietime':'0',
        'isgetcode':'1'}
#获取数据用data
now_time = datetime.datetime.now() + datetime.timedelta(days=-1)
yes_time = now_time.strftime("%Y-%m-%d")
data2 = {
        'page_no':'1',
        'page_size':'500',
        'sortname':'undefined',
        'sortorder':'undefined',
        'fromdate':yes_time,
        'enddate':yes_time,}
data3 = {
        'page_no':'1',
        'page_size':'500',
        'sortname':'undefined',
        'sortorder':'undefined',
        'fromdate':yes_time,
        'todate':yes_time,
        'trucktype': '2',
        'orgcode': '10009801',
        'truckweighttype': 'undefined',
        'usetypeid':''
}
s = requests.session()
res1 = s.post(url1, data=data, headers=headers)
print(json.loads(res1.content.decode('utf-8')))

def shiyong():
    res2 = s.post(url2,cookies=res1.cookies,data=data2,headers=headers)
    res3 = json.loads(res2.content.decode())
    print(res3)
    with open('a.txt','w') as f:
        json.dump(res3,f)

def youhao():
    res4 = s.post(url3, cookies=res1.cookies, data=data3, headers=headers)
    print(res4.content)
    res5 = json.loads(res4.content.decode())
    print(res5)
    with open('b.txt', 'w') as f:
        json.dump(res5, f)
