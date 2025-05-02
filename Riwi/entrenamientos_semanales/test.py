while True:
    Notas = []
    while True: 
            nombre = input("Ingrese el nombre del estudiante por favor: ")
            if  nombre.replace(" ", "").isalpha():
                break
            else:
                print("Ingrese un nombre valido\n")
    
    while True:
        cadenaNotas = input("Ingrese por favor una lista de notas separas por comas(,): ")       
        notasTemp = cadenaNotas.split("," )

        notasValidas = True
        for i in notasTemp:
            try:
                float(i)
            except ValueError:
                notasValidas = False
                

                
        if notasValidas == True:
            notasTemp = [float(note) for note in notasTemp]
            rangoFuera = False
            for i in notasTemp:
                if not 1 <= i <=100:
                    rangoFuera = True
                    break
            if rangoFuera:
                print("Una o más notas están fuera del rango permitido (1-100). Intente de nuevo.") 
            else:
                Notas = notasTemp
                
                print("Notas agregadas con exito") 
                break    
        else:
            print("Una o más notas no son validas. Intente de nuevo")                                   
    salir = int(input("¿Quieres ingresar las notas para mas estudiantes? 1 para si, 2 para no: "))
    if salir == 2:
        break
print(Notas)
print("Programa finalizado")

