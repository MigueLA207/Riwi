notasEstudiante = {}


def mostrar(notasEstudiante):
    print("\n--- Mostrar notas ---")
    for nombre, notas in notasEstudiante.items():
        notas_formateadas = ""
        for i, nota in enumerate(notas):
            notas_formateadas += str(nota)
            notas_formateadas += ", "
        print(f"{nombre}: {notas_formateadas}")
    print("--------------------------\n")



print("╔═════════════════════════════════════════════════════════════╗") 
print("║                        GESTOR DE NOTAS                      ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")



#Preguntar opcion del menu:
while True:

    print("Bienvenido al crud estas son las opciones que tenemos disponibles: ")
    print("1.Agregar nuevo estudiante")
    print("2.Hallar promedio de estudiante")
    print("3.Notas mayores a")
    print("4.Notas repetidas")
    print("5.Salir")
    
    while True: 
        entrada = input("Escoge una opción del menú: ")
        if entrada.isdigit():
            opcion = int(entrada)
            if opcion >= 1 and opcion <=5:
                break
            else:
                print("Ingrese una de las opciones posibles\n")
       


    match opcion:
        case 1:
            while True:
                notas = []
                while True: 
                    nombre = input("Ingrese el nombre del estudiante por favor: ")
                    if  nombre.replace(" ", "").isalpha():
                        break
                    else:
                        print("Ingrese un nombre valido\n")
                        
                whileValidation = True
                
                while whileValidation:    
                    datos = input("Digite una lista de notas separadas por ','. Si el numero es decimal lo separa por '.': ")
                    lista_valores = datos.split(",")
                    
                    converter = []
                    for i in lista_valores:
                        if i.isdigit():
                            i = float(i)
                            converter.append(i)
                        else:
                            whileValidation = False
                            
                    lista_valores = converter     
                    print(lista_valores)
                    
                    for n in lista_valores:
                        if not 1 <= n <=100:
                            print("malo")
                            whileValidation = False
                        else:
                            notas.append(n)
                            
                salir = int(input("¿Quieres ingresar las notas para mas estudiantes? 1 para si, 2 para no: "))
                
                if salir == 2:
                    break

            mostrar(notasEstudiante)


    


        case 2:
            mostrar(notasEstudiante)
            
            while True: 
                nombreOp = input("Ingresa porfavor el nombre de la persona a la que le quieres hallar el promedio: ")
                if  nombreOp.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese un nombre valido\n")

            if nombreOp in notasEstudiante:
                
                notis = notasEstudiante[nombreOp]
                print(f"opcion a calcular: {notis}")
                
                sumatoria = 0
                contador = 0
                for i in notis:
                    sumatoria += i
                    contador +=1

                promedio = sumatoria/contador
                
                if promedio < 50:
                    print(f"Reprobaste, tu promedio es: {promedio}")
                elif promedio >= 50 and promedio < 70:
                    print(f"Aprobaste, bien hecho, tu promedio es: {promedio}")
                else:
                    print(f"Sobresaliente, felicitaciones, tu promedio es: {promedio}")
            else:

                print(f"No se encontraron notas para el estudiante {nombreOp}. Intente de nuevo.")   

            otro = int(input("¿Quieres calcular el promedio de otro estudiante? 1 para sí, 2 para no: "))
            if otro == 2:
                break
            
            
            
            
            
        case 3:
            print("---------Numeros mayores---------")
            mostrar(notasEstudiante)
            
            while True: 
                nombreOp = input("Ingresa porfavor el nombre del estudiante para hallar la nota mayor:  ")
                if nombreOp in notasEstudiante:
                    notis = notasEstudiante[nombreOp]
                    break
                else:
                    print("ese nombre no se encuentra en la lista de estudiantes. Intente de nuevo")                
                
            mayores = []
            while True:
                mayor = int(input("Ingrese una nota y te mostrare las mayores a esta: "))
                if mayor in notis:
                    for i in notis:
                        if mayor < i:
                            mayores.append(i) 
                    print(f"Las notas mayores a {mayor} son: {mayores} ")  
                    break
                else:
                    print("No se encuentra. intente de nuevo") 
            print("--------------------------------")

            otro = int(input("¿Quieres hacerlo para otro estudiante? 1 para sí, 2 para no: "))
            if otro == 2:
                break
            
            
            

        case 4:

            mostrar(notasEstudiante)
            while True: 
                nombreOp = input("Ingresa porfavor el nombre de un estudiante para verificar cuantas se repiten: ")
                if nombreOp in notasEstudiante:
                    notis = notasEstudiante[nombreOp]
                    break
                else:
                    print("ese nombre no se encuentra en la lista de estudiantes. Intente de nuevo")
            
            repetidos = 0
            while True:
                repetido = int(input("Ingrese una nota y te mostrare cuantas veces se repite: "))
                if repetido in notis:
                    for i in notis:
                        if repetido == i:
                            repetidos += 1 
                    print(f"Las nota {repetido} se repite {repetidos} veces ")  
                    break
                else:
                    print("No se encuentra. intente de nuevo") 
            print("--------------------------------")

            otro = int(input("¿Quieres hacerlo para otro estudiante? 1 para sí, 2 para no: "))
            if otro == 2:
                break
                    
            
        
            

                
            
        
    



    
    
    
    
    



