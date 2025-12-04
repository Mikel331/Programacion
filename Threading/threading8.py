import threading
import time

def numeros_Ascendente(num1, num2):
    global resultado
    for i in range(1,9):
        print(i)
        resultado = num1 - num2
        
def numeros_Descendentes(num2,num1):
    global resultado
    for i in range(9,1,-1):
        print(i)
        resultado = num2 - num1
               
def factorial(numeros):
    global resultado
    for i in range(1,numeros+1):
        print(i)
        resultado *=i
        print("Multiplicando:" , i , "resultado:" , resultado)
        

        
        
if __name__ == "__main__":
    t = threading.Thread(target=numeros_Ascendente, args=(1,9))
    t.start()
    time.sleep(1)
    t = threading.Thread(target=numeros_Descendentes, args=(9,1))
    t.start()
    time.sleep(2)
    
    t= threading.Thread(target=factorial, args=(5,))
    t.start()
    time.sleep(3)
    print("El factorial es: " , resultado)
    

   