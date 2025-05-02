lista = [1,3,6,9,12]
print(f"La lista es: {lista}")
numero = int(input("Ingrese un numero para buscar en la lista: "))

if numero in lista:
    indice = lista.index(numero)
    print(f"El numero {numero} si esta en la lista, y su indice es {indice} ")
    