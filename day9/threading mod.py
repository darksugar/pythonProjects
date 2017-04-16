#Author:Ivor
import threading
import time
def run(n):
    print("task---start,",n)
    time.sleep(1)
    print("task---end",n,threading.current_thread())
res_list = []
start_time = time.time()
#Starting Multiple threads
for i in range(50):
    t = threading.Thread(target=run,args=("t %s" % i,))
    #set child threads to daemon threads
    t.setDaemon(True)
    t.start()
    res_list.append(t)
#Main Thread waiting for the child threads
for r in res_list:
    r.join()

print("current thread",threading.current_thread())
print("Running time = ",time.time() - start_time)
