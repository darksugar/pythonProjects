#Authon Ivor
import pickle

def sayhi():
    print("Hello World!")

info = {
    "name":"Ivor",
    "func":sayhi
}

with open("pickle.pickle","wb") as f:
    f.write(pickle.dumps(info))

with open("pickle.pickle", "wb") as f:
    pickle.dump(info,f)

