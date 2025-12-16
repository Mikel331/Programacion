import threading
import time
import random

buffer = []
MAX_ITEMS = 3
NUM_ITEMS = 10
semaforo = threading.Semaphore(4)

def productor():
    for i in range(NUM_ITEMS):
        semaforo.acquire()
        while len(buffer) >= MAX_ITEMS:
            pass  

        item = f"item-{i}"
        buffer.append(item)
        print(f"Produce {item},Buffer{buffer}")
        time.sleep(random.random() / 10)
        semaforo.release()

def consumidor():
    for i in range(NUM_ITEMS):
        semaforo.acquire()
        while len(buffer) == 0:
            pass

        item = buffer.pop(0)
        print(f"Consume {item},Buffer{buffer}")
        time.sleep(random.random() / 10)
        semaforo.release()

t_prod = threading.Thread(target=productor, name="productor")
t_prod = threading.Thread(target=productor, name="producto2")
t_cons = threading.Thread(target=consumidor, name="consumidor")
t_cons = threading.Thread(target=consumidor, name = "consumidor2")

t_prod.start()
t_cons.start()

t_prod.join()
t_cons.join()

print("Fin del main (pero los hilos pueden seguir ejecutándose)")
