archivo = "C:\\Users\\ikmsuarez23\\Desktop\\Programacion\\EjercicioClase\\LoremIpsum.txt"

with open(archivo, "r+", encoding="utf-8") as archivos:

    lista = [["Hola", "Adios"], ["Que tal", "Bien"] , ["Siiiiiii", "Nooooo"]]
    tupla = (1,2,3,4)
    palabras=archivos.read().split(" ")
    palabras.sort()
    
    archivos.write("Contenido añadido\n" )
    archivos.write("------------------\n")
    for fila in lista:
        archivos.write("," .join(fila)+ "\n")
        archivos.write(",".join(map(str,tupla))+ "\n")
    
    for palabra in palabras:
        archivos.write(palabra + " ")

print(palabras)