import random

"""LEE EL ARCHIVO Y AÑADE EL JUGADOR"""
palabrasArchivo = r"C:\Users\ikmsuarez23\Desktop\Programacion\Ahorcado\palabras.txt"
puntuaciones = r"C:\Users\ikmsuarez23\Desktop\Programacion\Ahorcado\Puntuaciones.txt"

with open(palabrasArchivo,"r+",encoding="utf-8") as archivo, open(puntuaciones,"w+") as puntuacion:
        juegos_palabras= archivo.read()
        nombre=(input("Introduce el nombre:"))
        puntuacion.write(nombre + " ")
        

"""CREACION DE LAS LISTAS POR NIVELES"""
Palabras_facil = ["gato","casa","mesa","playa","coche","queso","flor","libro","perro","nube"]
Palabras_medio = ["montaña","ventana","elefante","sombrero","planeta","misterio","zapatero","espejo","biblioteca","castillo"]
Palabras_dificil = ["mariposa","arquitectura","extraordinario","programador","electricidad","melancolía","universidad","laboratorio","meteorología","descubrimiento"]

intentos = 6;
acierto = True

"""METODOS DE LOS NIVELES"""
def opcion1():
        print("Has elegido el nivel facil")
        palabra = random.choice(Palabras_facil)
        palabra_oculta ="_"*len(palabra)
        print(f"La Palabra elegida es: {palabra_oculta}")
        
        for i in range(intentos):
            
            letras = input(f"Adivina {palabra_oculta}(Intentos restantes {intentos-i})").lower() 
            
            relleno_palabra = ""
            for j in range(len(palabra)):
                if palabra[j] == letras:
                    relleno_palabra +=letras
                    print(relleno_palabra)
                else:
                    relleno_palabra += palabra_oculta[j]

            palabra_oculta = relleno_palabra  
            print(f"Palabra actual: {palabra_oculta}")
            
        if palabra_oculta == palabra:
            print(f"Has acertado la palabra: {palabra}")
        
        if palabra_oculta!=palabra:
                print(f"Has fallado la palabra: {palabra}")
               
    
        with open(puntuaciones, "a", encoding="utf-8") as puntuacion:      
                puntuacion.write(palabra + " ")
                puntuacion.write(relleno_palabra + " ")
        input("Presiona Enter para volver al menú...") 
        
        
            
def opcion2():
        print("Has elegido el nivel medio")
        palabra = random.choice(Palabras_medio)
        palabra_oculta ="_"*len(palabra)
        print(f"La Palabra elegida es: {palabra_oculta}")

        for i in range(intentos):
            letras = input(f"Adivina {palabra_oculta}(Intentos restantes {intentos-i})").lower()  
            
            relleno_palabra = ""
            for j in range(len(palabra)):
                if palabra[j] == letras:
                    relleno_palabra +=letras
                else:
                    relleno_palabra += palabra_oculta[j]

            palabra_oculta = relleno_palabra
            print(f"Palabra actual: {palabra_oculta}")   
    
        if palabra_oculta == palabra:
            print(f"Has acertado la palabra: {palabra}")
            
        if palabra_oculta!=palabra:
            print(f"Has fallado la palabra: {palabra}")
            
        with open(puntuaciones, "a", encoding="utf-8") as puntuacion:      
                puntuacion.write(palabra + " ")
                puntuacion.write(relleno_palabra + " ")
        input("Presiona Enter para volver al menú...") 
    

def opcion3():
        print("Has elegido el nivel dificil")
        palabra = random.choice(Palabras_dificil)
        palabra_oculta ="_"*len(palabra)
        print(f" La Palabra elegida es: {palabra_oculta}")

        for i in range(intentos):
                letras = input(f"Adivina {palabra_oculta}(Intentos restantes {intentos-i})").lower()  
                
                relleno_palabra = ""
                for j in range(len(palabra)):
                    if palabra[j] == letras:
                        relleno_palabra +=letras
                    else:
                        relleno_palabra += palabra_oculta[j]

                palabra_oculta = relleno_palabra 
                print(f"Palabra actual: {palabra_oculta}") 
                
        if palabra_oculta == palabra:
                print(f"Has acertado la palabra: {palabra}")
         
        if palabra_oculta!=palabra:
            print(f"Has fallado la palabra: {palabra}")
                
        with open(puntuaciones, "a", encoding="utf-8") as puntuacion:      
                puntuacion.write(palabra + " ")
                puntuacion.write(relleno_palabra + " ")
        input("Presiona Enter para volver al menú...")


def salir():
        print("Saliendo....")
        input("Presiona Enter para volver al menú...") 
        return True
    

opciones = {
        '1': opcion1,
        '2': opcion2,
        '3': opcion3,
        '4': salir,   
    }

"""MUESTRA DEL ARCHIVO"""
print(juegos_palabras)

while True:


        """MENU"""
        print("-------------")
        print("Menu Ahorcado")
        print("-------------")
        print("1.Facil")
        print("2.Medio")
        print("3.Dificil")
        print("4.Salir")

        elegir = input("Elige la dificultad con la que quieres jugar")
        

        if elegir in opciones:
            opciones[elegir]()
            
        else:
            print("error")
            