import threading

def thread_apellido (name, inicio=1, fin=1):
    for x in range(inicio,fin):
        print(f"{name} Rodriguez {str(x)} años\n", end="")
        
nombres ={"Julio", "Javier", "Eladio", "Jose", "Manuel"}
hilos = list()
for n in nombres:
    t= threading.Thread(target=thread_apellido,args=(n,), kwargs={'inicio':5 , 'fin':8})
    hilos.append(t)
    t.start()
