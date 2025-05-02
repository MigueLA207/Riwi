lista = [1,2,3,4,5]
print(f"Lista actual: {lista}")
agregar = int(input("Digite el numero para ingresar en la lista: "))
indice = int(input("Digite la posicion en la que quiere agregar el numero: "))

lista.insert(indice-1, agregar)

print(f"Lista actualizada: {lista}")

