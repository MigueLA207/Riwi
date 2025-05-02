print("╔═════════════════════════════════════════════════════════════╗") 
print("║                      LISTA DE PRODUCTOS                     ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

# Definimos lo necesario para el programa
productos = []
total = 0

# Utilizamos el while True para repetir el codigo en caso de que el try halle alguna excepcion

while True:
    
    porcentaje_descuento=0
    #Verificamos el nombre del producto
    while True:
        try:
            nombre_producto = str(input("Ingresa el nombre del producto: "))

            if nombre_producto.isalpha():
                break
            else: 
                print("Ingrese un nombre valido")            
        
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
        except ValueError:
            print("ingresa un dato valido por favor")


    #Verificamos el precio_unitario
    while True:
        try:
            precio_unitario = float(input("Ingresa el precio del producto: "))

            if precio_unitario > 0:
                break
            else: 
                print("Ingrese un valor positivo")            
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
        except ValueError:
            print("ingresa un dato valido por favor")


    #Verificamos el precio_unitario
    while True:
        try:
            cantidad_productos = int(input("Ingresa la cantidad de productos: "))
            if cantidad_productos >= 0:
                break
            else: 
                print("Ingrese un valor positivo")            
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario")
        except ValueError:
            print("ingresa un dato valido por favor")
            


    #Verificamos que el porcentaje sea valido
    while True:
        try:
            porcentaje_descuento = int(input("Ingresa el porcentaje de descuento a aplicar(0% - 100%): "))
            if  0 <= porcentaje_descuento <= 100:
                break 
            else: 
                print("Ingrese un valor en el rango de 0 - 100")            
        except KeyboardInterrupt:
                print("\nPrograma interrumpido por el usuario") 
        except ValueError:
            print("ingresa un dato valido por favor")  
    
    #Agregamos el producto a la lista con los datos que el usuario ingreso
    productos.append([nombre_producto,precio_unitario,cantidad_productos,porcentaje_descuento])
    
    
    #Verificamos que la opcion ingresada si este en las opciones
    while True:
        try:
            seguir = int(input("\nDigite 1 si quiere agregar mas productos, digite 2 si quiere ver su factura:  \n"))
            if seguir >=1 and seguir <=2:
                break
            else: 
                print("Ingrese una de las opciones posibles")            
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
        except ValueError:
            print("No estas ingresando un numero o el numero no es entero")
    
    if seguir == 2:
        break
        
    


#para mostrar algo en pantalla de manera espaciada y ordenada utilizamos (:<#), # = numero de espacios al 
#cual debe estar alineado con respecto al texto de f-string donde sea utilizado
# Modificamos la cabecera para incluir el descuento
print("―" * 25 + " Factura " + "―" * 26,"\n")
print(f"| {'Nombre producto':<15} | {'Costo Unit':<10} | {'Cantidad':<10} | {'Descuento %':<11} |")
print("-" * 60)

for valor in productos:
    print(f"| {valor[0]:<15} | {valor[1]:<10.2f} | {valor[2]:<10} | {str(valor[3]) + '%':<11} |")

    subtotal = valor[1] * valor[2]
    descuento = subtotal * (valor[3] / 100)
    subtotal_descuento = subtotal - descuento
    total += subtotal_descuento

print("-" * 60)
print(f"| {'Total con descuentos:':<42} | {total:>10.2f} |")
print("―" * 60)

print("\nFin del programa")

    
                    
    
    
    