#Authon Ivor
import threading
import time

def light():
    count = 0
    #initialize signal
    cond.set()
    while True:
        if count > 5 and count < 10:
            #clear signal
           cond.clear()
           print("\033[41;1mRed light\033[;0m")
        elif count > 10:
            #set signal
            cond.set()
            count = 0
        else:
            print("\033[42;1mGreen light\033[;0m")
        count += 1
        time.sleep(1)

def car():
    while True:
        time.sleep(1)
        if cond.is_set():
            print("Car gogo...")
        else:
            print("Car stop...")
            #hang on the thread
            cond.wait()

cond = threading.Event()
l = threading.Thread(target=light)
c = threading.Thread(target=car)
l.start()
c.start()