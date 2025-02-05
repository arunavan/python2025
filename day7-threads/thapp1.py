import threading
import time
def print_series():
    for i in range(0,10,2):
        time.sleep(1)
        print(time.ctime(time.time()))
        print(i)
t1=threading.Thread(target=print_series)
t2=threading.Thread(target=print_series)
t1.start()
t2.start()
print('Active Count',threading.active_count)

t1.join()
t2.join()