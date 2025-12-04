import threading 
import time

Palabras = {"Queso", "Amarillo", " Camion", "Autobus", "Botella"}

def Mayuscula (palabras_Mayuscula):
    
    for palabras_Mayuscula in Palabras:
        print(palabras_Mayuscula.upper())
        
    
def Minuscula (palabras_Minuscula):
    for palabras_Minuscula in Palabras:
        print(palabras_Minuscula.lower())
        

if __name__ == "__main__":
    t1 = threading.Thread(target=Mayuscula, args=(Palabras,))
    t1.start()
    t1.join()
    
    t2=threading.Thread(target=Minuscula, args=(Palabras,))
    t2.start()
    t2.join()
        