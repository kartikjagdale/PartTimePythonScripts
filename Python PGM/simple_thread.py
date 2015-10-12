import threading
TOTAL = 0
GRID_LOCK = threading.Lock()
class cnt(threading.Thread):
    def run(self):
        global TOTAL
        GRID_LOCK.acquire()
        for i in range(100000):
            
            TOTAL=TOTAL+1
            
        print('%s\n'%(TOTAL))
        GRID_LOCK.release()
           
a = cnt()
b = cnt()
a.start()


#GRID_LOCK.acquire()

b.start()
#GRID_LOCK.release()
