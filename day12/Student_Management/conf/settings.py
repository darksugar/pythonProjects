#Authon Ivor
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logging

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
    'manage':'management.log'
            }

db_user = "root"
db_pass = "mysql123"
db_ip = "127.0.0.1"
db_port = "3306"
db_name = "student_management"
