#Author:Ivor#Authon Ivor

import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_HOME = "%s/home" %base_dir
LOG_DIR = "%s/log" %base_dir
LOG_LEVEL = 'DEBUG'
ACCOUNT_FILE = "%s/conf/accounts.cfg" %base_dir


HOST = '127.0.0.1'
PORT = 9999