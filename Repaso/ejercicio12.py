numero1 = int (input("Introduce el primer numero"))
numero2 = int(input("Introduce el segundo numero"))

print("Seleccione el calculo que quiere realizar")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")

opcion= (int (input("Introduce un numero del 1-4")))

match opcion :
    case 1 :
        resultado = numero1 + numero2 
    case 2 :
        resultado = numero1 - numero2
    case 3 :
        resultado = numero1 * numero2
    case 4 :
        resultado = numero1 / numero2

print ("Resultado", resultado)

    


