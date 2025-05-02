frutas = ["Mango", "Arroz", "Pera"]
print(f"Lista de frutas: {frutas}")
eliminar = input("Digite el nombre de lo que quiere eliminar: ")
if eliminar in frutas:
    frutas.remove(eliminar)
    print("Dato eliminado")
    
print(f"lista actualizada: {frutas}")