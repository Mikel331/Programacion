import threading
import random

def mostrar(d):
    try:
        val = d.valor
    except AttributeError:
        print(f"(threading.current_thread().name: Aun no inicializando\n" , end="")
    else:
        print(f"(threading.current_thread().name: {val}\n)", end="")
    

def hilo(dato):
    mostrar(dato)
    dato.valor = random.randint(1,100)
    mostrar(dato)

if __name__ == "__main__":  
    dato = threading.local()
    mostrar(dato)
    dato.valor=999
    mostrar(dato)

    for i in range(3):
        t= threading.Thread(target=hilo, args=(dato,))
        t.start()
    
        