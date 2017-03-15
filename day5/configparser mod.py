#Authon Ivor

import configparser
#新增
config = configparser.ConfigParser()
config["DEFAULT"] = {
    "port":5506,
    "enable":"YES"
}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
#修改
config["DEFAULT"]["enable"] = "NO"
a = config.sections()

print(a)

#写入
with open("conf.ini","w") as f:
    config.write(f)

#读取
config.read("conf.ini")
print(config.sections())
print(config.items())
print(config.keys())
print(config.values())

# ########## 读 ##########

# secs = config.sections()

# print secs

# options = config.options('group2')

# print options



# item_list = config.items('group2')

# print item_list



# val = config.get('group1','key')

# val = config.getint('group1','key')



# ########## 改写 ##########

# sec = config.remove_section('group1')

# config.write(open('i.cfg', "w"))

# sec = config.has_section('wupeiqi')

# sec = config.add_section('wupeiqi')

# config.write(open('i.cfg', "w"))

# config.set('group2','k1',11111)

# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')

# config.write(open('i.cfg', "w"))