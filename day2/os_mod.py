#Author:Ivor

import os

#os.system('dir')
cmd_rst = os.popen('dir')
cmd_rst = os.popen('dir').read()
print(cmd_rst)

