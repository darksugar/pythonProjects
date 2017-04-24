#Authon Ivor
import time
import os
import pickle
file = open("1.2.exe", 'rb')
data = file.read(947)
a = {"action":"put",
     "detail":"put_file",
     "line":data
                    }
print(len(pickle.dumps(a)))