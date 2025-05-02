import sys
print("╔═════════════════════════════════════════════════════════════╗") 
print("║                    VALIDACIÓN DE PRODUCTOS                  ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

Usuarios = []
continuar0=True
while continuar0: 
    continuar1 = True
    continuar2 = True
    continuar3 = True
    continuar4 = True
    continuar5 = True
    opcion = 0
    print("Bienvenido al crud estas son las opciones que tenemos disponibles: ")
    print("1.Crear un nuevo usuario")
    print("2.Mostrar usuarios")
    print("3.Actualizar usuario")
    print("4.Eliminar un usuario")
    print("5.Salir")
    


    while continuar4:
            try:
                opcion = int(input("Escoge una opcion del menu: "))
                if opcion >=1 and opcion <=5:
                    continuar4 = False
                else: 
                    print("Ingrese una de las opciones posibles")            
                
            except ValueError:
                print("No estas ingresando un numero")


    #Hacer menu de opciones

    match opcion:
        case 1:
                print("\n","-" * 15,"crear un nuevo usuario","-" * 15,"\n")
                
                while continuar1:
                    try:
                        nombre = str(input("Ingresa el nombre por favor: "))   
                        continuar1 = False        
                    except ValueError:
                        print("No estas ingresando una cadena de texto, Ingresa un valor valido")

                while continuar2:
                    try:
                        apellido = str(input("Ingresa el apellido por favor: "))   
                        continuar2 = False        
                    except ValueError:
                        print("No estas ingresando una cadena de texto, Ingresa un valor valido")
                    

                 
            

                while continuar3:
                    try:
                        edad = int(input("Ingresa la edad porfavor: "))
                        if edad >= 0:
                            continuar3 = False
                        else: 
                            print("Ingrese un valor positivo")            
                        
                    except ValueError:
                        print("No estas ingresando la edad, Ingresa un valor valido")
                        
                    
                    correo=str(input("Ingresa el correo por favor: ")) 
                
                # while continuar5:
                #     for valor in Usuarios:
                #         correo=str(input("Ingresa el correo por favor: "))
                #         if correo == valor[2]:
                #             print("Correo ya exitente")
                #         else:
                #             
                #             continuar5 = False
                    Usuarios.append([nombre,apellido,correo,edad])   
                        
                
                print("\n","-"*40) 
            
        case 2:
                print("\n","-" * 15,"Mostrar Usuarios","-" * 15,"\n") 
                print(f"{'Nombre':<5} {'apellido':<10} {'correo':<10} {'edad':<10}")
                print("-" * 35)
                for valor in Usuarios:
                    print(f"{valor[0]:<10} {valor[1]:<10} {valor[2]:<10} {valor[3]:<10}")
                print("\n","-"*40) 
                
                
        case 3:
            #lista = [["miguel", "apellido", 15, "Corre"]]
                print("\n","-" * 15,"Actualizar usuarios","-" * 15, "\n")
                print("Estos son los usuarios que hay en el programa: ")
                print(f"{'id':<5}{'Nombre':<10} {'apellido':<10} {'correo':<10} {'edad':<10}")
                print("-" * 35)
                for valor in Usuarios:
                    id = Usuarios.index(valor)
                    print(f"{id+1:<5}{valor[0]:<10} {valor[1]:<10} {valor[2]:<10} {valor[3]:<10} ")
                
                id_editar = int(input("Ingresa en el numero del id que quieres editar: "))
                while continuar1:
                    try:
                        nombre = str(input("Ingresa el nombre por favor: "))   
                        continuar1 = False        
                    except ValueError:
                        print("No estas ingresando una cadena de texto, Ingresa un valor valido")

                while continuar2:
                    try:
                        apellido = str(input("Ingresa el apellido por favor: "))   
                        continuar2 = False        
                    except ValueError:
                        print("No estas ingresando una cadena de texto, Ingresa un valor valido")
                    

                correo = str(input("Ingresa el correo por favor: "))   

                while continuar3:
                    try:
                        edad = int(input("Ingresa la edad porfavor: "))
                        if edad >= 0:
                            continuar3 = False
                        else: 
                            print("Ingrese un valor positivo")            
                        
                    except ValueError:
                        print("No estas ingresando la edad, Ingresa un valor valido")
                
                
                id_remplazar = id_editar-1
                
                if id_remplazar >=0 and id_remplazar  < len(Usuarios):
                    nuevo_usuario = [nombre, apellido, correo, edad]
                    Usuarios[id_remplazar] = nuevo_usuario
                    print(f"Usuario con ID {id_editar} ha sido actualizado.")
                else:
                    print(f"El ID {id_editar} no es válido.")
                
                
                
                # id_editar = 
        case 4:
                print("\n","-" * 15,"Eliminar Usuario","-" * 15,"\n")
                print("Estos son los usuarios que hay en el programa: ")
                print(f"{'id':<5}{'Nombre':<10} {'apellido':<10} {'correo':<10} {'edad':<10}")
                print("-" * 35)
                for valor in Usuarios:
                    id = Usuarios.index(valor)
                    print(f"{id+1:<5}{valor[0]:<10} {valor[1]:<10} {valor[2]:<10} {valor[3]:<10} ")
                
                id_eliminar = int(input("Ingresa en el numero del id que quieres eliminar: "))
                del Usuarios[id_eliminar-1]
                print(f"Usuario con ID {id_eliminar-1} ha sido eliminado.")
                
                print("\n","-"*40) 
        case 5:
            sys.exit()
                
    
        
    seguir = str(input("\nQuieres continuar en el programa (S/N):  \n")).upper
    if seguir == "N":
        continue0 = False      
    else:
        print("\n","-"*40,"\n")
        

    
    

            




    
            








