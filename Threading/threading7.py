from threading import *
import time

def hilo():
    time.sleep(1)
    print("Hola")
    
t= Thread(target=hilo)
t.daemon=True
t.start()