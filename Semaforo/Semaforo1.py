import threading
import time
class ThreadPool(object):
 def __init__(self):
    super(ThreadPool, self).__init__()
    self.active = []
    self.lock = threading.Lock()
 def makeActive(self, name):
    with self.lock:
        self.active.append(name)
 def makeInactive(self, name):
    with self.lock:
        self.active.remove(name)
def f(s, pool):
 with s:
    name = threading.current_thread().name
    pool.makeActive(name)
    print(f"{name} empezó")  
    time.sleep(0.5)
    pool.makeInactive(name)
    print(f"{name} terminó") 
pool = ThreadPool()
s = threading.Semaphore(3)
for i in range(10):
    t = threading.Thread(target=f, name="thread_"+str(i), args=(s, pool))
    t.start()