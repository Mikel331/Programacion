import threading
import time
import random

buffer = []
MAX_ITEMS = 3
NUM_ITEMS = 10
condicion = threading.Condition()

def productor():
    for i in range(NUM_ITEMS):  
      with condicion:
        condicion.wait()
        while len(buffer) >= MAX_ITEMS:
            pass  # el hilo se queda quemando CPU

        item = f"item-{i}"
        buffer.append(item)
        print(f"Produce {item}")
        time.sleep(random.random() / 10)
        condicion.notify()

def consumidor():
    for i in range(NUM_ITEMS):
        with condicion:
            condicion.wait()
            while len(buffer) == 0:
                pass

            item = buffer.pop(0)
            print(f"Consume {item}")
            time.sleep(random.random() / 10)
            condicion.notify()

t_prod = threading.Thread(target=productor, name="productor")
t_cons = threading.Thread(target=consumidor, name="consumidor")

t_prod.start()
t_cons.start()

with condicion:
    condicion.notify()
 
t_prod.join()
t_cons.join()

print("Fin del main (pero los hilos pueden seguir ejecutándose)")
