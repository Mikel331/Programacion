import threading
import time

lista_numeros = {1,2,3,4,5,6,7,8,9,10}

def numeros_pares(num_pares):
    
    for i in num_pares:
        if i %2 == 0:
            print("Los numeros pares son :", i)
            
            
def numeros_impares(num_impares):
    for i in num_impares:
        if i %2 !=0:
            print("Los numeros impares son" , i)
            
            
if __name__ == "__main__":
    
    t = threading.Thread(target=numeros_pares, args=(lista_numeros,))
    t.start()
    time.sleep(1)
    
    t = threading.Thread(target=numeros_impares, args=(lista_numeros,))
    t.start()
    time.sleep(1)
    
            