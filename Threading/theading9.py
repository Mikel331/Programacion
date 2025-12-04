import threading
import time

suma = 0
def suma_Ascendente (num1, num2):
    global suma
    for i in range(1,20):
        print(i)
        suma = num1 + num2
        
def suma_Descendente(num2, num1):
    global suma
    for i in range (20,1,-1):
        print(i)
        suma = num2 + num1
       
        
        
def suma_Todos(numeros):
    global suma
    for i in range(1,numeros+1):
        suma +=i
        print("Sumando:" , i , "El resultado seria:" , suma)
        
 
if __name__ == "__main__":    
    t= threading.Thread(target=suma_Ascendente, args=(1,20))
    t.start()
    print("El resultado de la suma ascendente es de: " , suma)
    time.sleep(1)
   
    t = threading.Thread(target=suma_Descendente , args=(20,1))
    t.start()
    print("El resultado de la suma descendente es de: " , suma)
    time.sleep(2)
  
    t = threading.Thread(target=suma_Todos , args=(1,))
    t.start()
    print("El resultado de la suma de todo es de : " , suma)
    time.sleep(3)
    
 

 
  
        