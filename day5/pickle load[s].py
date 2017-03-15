#Authon Ivor

import pickle

def sayhi():
    print("Hello World!")

with open("pickle.pickle","rb") as f:
    pickle.loads(f.read())

with open("pickle.pickle","rb") as f:
    pickle.load(f)

