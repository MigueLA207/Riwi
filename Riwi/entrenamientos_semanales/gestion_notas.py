continuar = True
notas = []
sumatoria = 0
n = 0
while continuar:
    datos = str(input("Digite una lista de notas separadas por ','. Si el numero es decimal lo separa por '.': "))
    lista_valores = datos.split(",")
    print(lista_valores)
    
    for valor in lista_valores:
        notas.append(float(valor))
    
    salir = int(input("1 para salir, 2 para agregar mas notas: "))
    if salir == 1:
        break
    
    
print(notas)

for nota in notas:
    sumatoria += nota
    n +=1
    
promedio = sumatoria/n

print(f"El promedio de notas es de {promedio: .1f}")


