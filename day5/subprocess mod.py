#Authon Ivor

import subprocess

#执行命令，返回命令执行状态 ， 0 or 非0
retcode = subprocess.call(["ls", "-l"])

#执行命令，如果命令结果为0，就正常返回，否则抛异常
subprocess.check_call(["ls", "-l"])

#接收字符串格式命令，返回元组形式，第1个元素是执行状态，第2个是命令结果
subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')

#接收字符串格式命令，并返回结果
subprocess.getoutput('ls /bin/ls')
'/bin/ls'

#执行命令，并返回结果，注意是返回结果，不是打印，下例结果返回给res
res=subprocess.check_output(['ls','-l'])
res
b'total 0\ndrwxr-xr-x 12 alex staff 408 Nov 2 11:05 OldBoyCRM\n'

#上面那些方法，底层都是封装的subprocess.Popen
res.poll()
# Check if child process has terminated. Returns returncode
res.wait()
# Wait for child process to terminate. Returns returncode attribute.

res.terminate()
# 杀掉所启动进程
res.communicate()
# 等待任务结束
# stdin 标准输入
# stdout 标准输出
# stderr 标准错误
res.pid
# The process ID of the child process.

#例子
p = subprocess.Popen("df -h|grep disk",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
p = subprocess.Popen(['df','-h'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)
p.stdout.read()
b'/dev/disk1 465Gi 64Gi 400Gi 14% 16901472 104938142 14% /\n'

# 可用参数：
# •args：shell命令，可以是字符串或者序列类型（如：list，元组）
# •bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
# •stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
# •preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
# •close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
# 所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
# •shell：同上
# •cwd：用于设置子进程的当前目录
# •env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
# •universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
# •startupinfo与createionflags只在windows下有效
# 将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等