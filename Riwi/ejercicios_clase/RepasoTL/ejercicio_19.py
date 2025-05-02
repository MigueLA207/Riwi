pares = []
for i in range(5):
    num = int(input("ingresa un numero: "))
    if num % 2 == 0:
        pares.append(num)
        print(f"El numero {num} es par. Agregado con exito")
    else:
        print(f"El numero {num} no es par") 

print(f"La lista de pares es: {pares}")