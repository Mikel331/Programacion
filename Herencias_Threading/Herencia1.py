import threading 
class miHilo(threading.Thread):
    def __init__(self,num):
        super(miHilo,self).__init__()
        self.numero = num
        self.nombre = ""
        
    def run(self):
        if self.nombre =="hiloPar":
            print(f'par:{self.numero}\n' ,end='')
        else:
            print(f'impar: {self.numero}\n' ,end='')   
            
ListaHilos = []
for i in range(10):
    t=miHilo(i) 
    if (i%2)==0:
        t.nombre = "hiloPar"
    else:
        t.nombre="hiloImpar"
    ListaHilos.append(t)

for h in ListaHilos:
    h.start()
    
for h in ListaHilos:
    h.join()
    