import threading 
import time 
  
ev = threading.Event()
barrera = threading.Barrier(3)

def evento():
    for i in range (3):
        print("Esta listo y esperando...")
        time.sleep(2)
        ev.set()
    

def trabajador():
    ev.wait()
        
    print(f"{threading.current_thread().name} Esperando en la barrera...")
    time.sleep(2)
    barrera.wait()
    print(f"{threading.current_thread().name} Trabajador ha comenzado a trabajar")
   
threading.Timer(3, evento).start()
hilos= []
for nombre in range(3):
    t = threading.Thread(target=trabajador,name=f"trabajador{nombre+1}") 

    t.start()
    hilos.append(t)
    

    

    
    