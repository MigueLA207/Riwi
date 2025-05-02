import sys
notasEstudiante = {}

#Creamos una funcion para mostrar los estudiantes, ya que la tenemos que utilizar en varias partes del codigo
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

    print("\nBienvenido al crud estas son las opciones que tenemos disponibles: ")
    print("1.Agregar nuevo estudiante")
    print("2.Hallar promedio de estudiante")
    print("3.Notas mayores a")
    print("4.Notas repetidas")
    print("5.Salir")
    #Verificamos que la opcion este en el menu
    while True: 
        entrada = input("Escoge una opción del menú: ")
        if entrada.isdigit():
            opcion = int(entrada)
            if opcion >= 1 and opcion <=5:
                break
            else:
                print("Ingrese una de las opciones posibles\n")
       

    #Creamos casos segun la opcion que escoja el usuario
    match opcion:
        case 1:
            while True:
                Notas = []
                #Verificamos que el nombre no sea un numero y que pueda tener espacios
                while True: 
                        nombre = input("Ingrese el nombre del estudiante por favor: ")
                        if  nombre.replace(" ", "").isalpha():
                            break
                        else:
                            print("Ingrese un nombre valido\n")

                #Ingreso de notas separadas por (,)
                while True:
                    cadenaNotas = input("Ingrese por favor una lista de notas separas por comas(,): ")       
                    notasTemp = cadenaNotas.split("," )


                    #Validacion de que las notas si sean numeros
                    notasValidas = True
                    for i in notasTemp:
                        try:
                            float(i)
                        except ValueError:
                            notasValidas = False
                

                    #Validacion de que las notas si esten en el rango de 180
                    if notasValidas == True:
                        #Aplicamos la comprension de listas
                        notasTemp = [float(note) for note in notasTemp]
                        rangoFuera = False
                        for i in notasTemp:
                            if not 1 <= i <=100:
                                rangoFuera = True
                                break
                        if rangoFuera:
                            print("Una o más notas están fuera del rango permitido (1-100). Intente de nuevo.") 
                        else:
                            for i in notasTemp:
                                Notas.append(i)

                            notasEstudiante[nombre] = Notas
                            print("Notas agregadas con exito") 
                        
                            break    
                    else:
                        print("Una o más notas no son validas. Intente de nuevo")
                                        
                salir = int(input("¿Quieres ingresar las notas para mas estudiantes? 1 para si, 2 para no: "))
                if salir == 2:
                    break

            mostrar(notasEstudiante)

        case 2:
            print("---------Hallar Promedio---------")
            while True:
                mostrar(notasEstudiante)
                while True: 
                    nombreOp = input("Ingresa porfavor el nombre de la persona a la que le quieres hallar el promedio: ")
                    if  nombreOp.replace(" ", "").isalpha():
                        break
                    else:
                        print("Ingrese un nombre valido\n")

                if nombreOp in notasEstudiante:
                    #Guardamos las notas del estudiante en notasEst
                    notasEst = notasEstudiante[nombreOp]
                    print(f"opcion a calcular: {notis}")
                    
                    #Hacemos la sumatoria de las notas, y agregamos un contador para saber entre cuanto se debe dividir
                    sumatoria = 0
                    contador = 0
                    for i in notasEst:
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

            print("---------Notas mayores---------")
            mostrar(notasEstudiante)
            
            while True: 
                nombreOp = input("Ingresa porfavor el nombre del estudiante para hallar la nota mayor:  ")
                if nombreOp in notasEstudiante:
                    notasEst = notasEstudiante[nombreOp] #Si el nombre esta en las opciones agrega las notas de ese estudiante a notasEst
                    break
                else:
                    print("ese nombre no se encuentra en la lista de estudiantes. Intente de nuevo")                
                
            mayores = [] #Definimos mayores y ahi guardamos las notas que sean mayores a 'mayor'
            while True:
                mayor = int(input("Ingrese una nota y te mostrare las mayores a esta: "))
                if mayor in notasEst:
                    for i in notasEst:
                        if mayor < i: #Con esta condicion verificamos si la nota es mayor o menor y la guarda en la lista segun el resultado
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
            print("---------Notas Repetidas---------")
            while True:
                mostrar(notasEstudiante)
                while True: 
                    nombreOp = input("Ingresa porfavor el nombre de un estudiante para verificar cuantas se repiten: ")
                    if nombreOp in notasEstudiante:
                        notis = notasEstudiante[nombreOp] #Si el nombre esta en las opciones agrega las notas de ese estudiante a notasEst
                        break
                    else:
                        print("ese nombre no se encuentra en la lista de estudiantes. Intente de nuevo")
                
                repetidos = 0
                while True:
                    repetido = input("Ingrese una nota y te mostrare cuantas veces se repite: ")
                    if repetido.isdigit():
                        repetido = int(repetido)
                    else:
                        print("Ingrese una de las opciones posibles\n")


                    if repetido in notis:
                        for i in notis:
                            if repetido == i: #Con esta condicion verificamos si el numero se encuentra en la lista
                                repetidos += 1 #En caso de ser verdadero se le suma a repetidos una unidad
                        print(f"Las nota {repetido} se repite {repetidos} veces ")  #Mostramos las veces que se repitio cierto numero
                        break
                    else:
                        print("No se encuentra. intente de nuevo") 
                print("--------------------------------")

                otro = int(input("¿Quieres hacerlo para otro estudiante? 1 para sí, 2 para no: "))
                if otro == 2:
                    break
        case 5:
            print("Fin de programa")
            sys.exit()
    

    
    
    
    
    



