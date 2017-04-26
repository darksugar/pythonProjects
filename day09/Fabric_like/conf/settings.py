#Authon Ivor
import uuid
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST_DIR = "%s/db/hosts" % BASE_DIR
GROUP_DIR = "%s/db/groups" % BASE_DIR

def get_new_id():
    return uuid.uuid1()