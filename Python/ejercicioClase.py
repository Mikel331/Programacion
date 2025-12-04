
listaNumeros = []
for lista in range(0,5):
    num= int (input("Dame cinco numeros"))
    listaNumeros.append(num)

listaNumeros.sort(reverse=True)

print("Lista ordenada", listaNumeros)
