import threading

def numero (num, resta):
    print("El numero es: " , num , " y el resultado de la resta es de :", resta)
    

valores = [3,10]
hilos = []
resta = 0

if (valores[0] < valores[1]):
        resta = valores[1] - valores[0]
        print(resta)
        
for i in valores: 

    if __name__ == "__main__":
        t= threading.Thread(target=numero, args=(i,resta))
        hilos.append(t)
        t.start()
       
        
    