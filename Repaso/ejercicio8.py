
array_vocales: str= ("a","e","i","o","u")
palabra: str=  "Habitacion".lower()

vocales = sum(1 for letra in palabra if letra in array_vocales)

print("Tiene " + str(len(palabra)) + " letras y " + str(vocales) + " vocales")

