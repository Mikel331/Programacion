import threading
import time
import random

ASIENTOS = 10
asientos = [False] * ASIENTOS   # False = libre, True = reservado

class cliente(threading.Thread):
    def __init__(self,nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        
        for _ in range(20):
            i = random.randint(0, ASIENTOS - 1)
            # Región crítica SIN proteger
            with lock:
                if not asientos[i]:
                    # simulamos que tardamos un poco en procesar
                    time.sleep(0.001)
                    asientos[i] = True
                    print(f"{self.nombre} reserva el asiento {i}")

                else:
                    print(f"{self.nombre} NO puede reservar el asiento {i} (ocupado)")
                    
    
                
            

hilos = []
lock = threading.Lock()
for i in range(5):
    t = cliente(f"cliente-{i}")
    hilos.append(t)
    t.start() 

for hilo in hilos:
    hilo.join()

print("Reservas terminadas (¿seguro?)")
print("Estado final de asientos:", asientos)