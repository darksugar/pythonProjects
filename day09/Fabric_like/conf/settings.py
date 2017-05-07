#Authon Ivor
import uuid
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST_DIR = "%s/db/hosts" % BASE_DIR
GROUP_DIR = "%s/db/groups" % BASE_DIR
FILE_DIR = "%s/tmp" % BASE_DIR

LOG_LEVEL = logging.INFO
LOG_FILE = "%s/log/action_log.txt" % BASE_DIR

def get_new_id():
    return uuid.uuid1()