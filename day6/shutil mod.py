#Authon Ivor

import shutil
#拷贝文件对象
f1 = open("random mod.py")
f2 = open("random_new.py","w")
shutil.copyfileobj(f1,f2,length=1)

#拷贝文件,文件和权限，包括copyfile和copymode
shutil.copy("random mod.py","random_new.py")
#拷贝文件和状态信息，包括copyfile和copystat
shutil.copy2("random mod.py","random_new.py")

#拷贝文件，不包括权限
shutil.copyfile("random mod.py","random_new.py")
#仅拷贝文件权限,仅拷贝权限。内容、组、用户均不变
shutil.copymode("random mod.py","random_new.py")
#拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat("random mod.py","random_new.py")

#拷贝文件目录，递归拷贝
shutil.copytree()
#递归删除
shutil.rmtree()
#移动文件
shutil.move()

shutil.make_archive()
#base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
# 如：www                        =>保存至当前路径
# 如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
# •format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# •root_dir： 要压缩的文件夹路径（默认当前目录）
# •owner： 用户，默认当前用户
# •group： 组，默认当前组
# •logger： 用于记录日志，通常是logging.Logger对象

import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()

# zipfile 压缩解压

import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()