lista = [1,3,1,9,4,4,9,3,1]
print(f"Mira la lista: {lista}")
buscar = int(input("Digita el numero del cual deseas saber su repeticion: "))
if buscar in lista:
    resultado = lista.count(buscar)
    print(f"El numero {buscar} se encuentra repetido {resultado} veces")
else:
    print("El numero no se encuentra en la lista")