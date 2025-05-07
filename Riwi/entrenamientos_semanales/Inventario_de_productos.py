inventario = {}

def agregar_producto(nombre,precio,cantidad):
    detalles_producto = {'Precio':float(precio) , 'Cantidad' : cantidad}
    inventario[nombre] = detalles_producto

def mostrar_inventario(inventario):
    print("\n-------------Mostrar notas-------------")
    for nombre, detalle in inventario.items():
        print(f"Nombre: {nombre} -- Precio: {detalle['Precio']} -- Cantidad: {detalle['Cantidad']}")
        
    print("----------------------------------------\n")
print("╔═════════════════════════════════════════════════════════════╗") 
print("║                     INVENTARIO DE PRODUCTOS                 ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")


print("\nOpciones disponibles: ")
print("\n(1).Añadir productos. \n(2).Consultar productos. \n(3).Actualizar . \n(4).Salir del programa") 


while True:
    opcion_menu = input("Ingresa una opcion del menu por favor: ")
    if opcion_menu.isdigit():
        break
    else: 
        print("Opcion invalida. Intenta de nuevo")
        
        
match opcion_menu:
    case "1":
        while True: 
            salir = True
            print("\n-------------Agregar Producto-------------\n")
            
            #Verificamos el nombre
            while True:
                nombre_producto = input("Ingrese por favor el nombre del producto: ")
                if nombre_producto.replace(" ", "").isalpha():
                    break
                else:
                    print("Opcion Invalida. Intente de nuevo ")
                    
            while True:    
                precio_producto = input("Ingrese por favor el precio del producto: ")
                if precio_producto.isdigit() and float(precio_producto) > 0:
                    precio_producto = float(precio_producto)
                    break
                else:
                    print("Opcion Invalida. Intente de nuevo")
            while True:
                cantidad_producto = input("Ingrese por favor la cantidad de productos que hay: ")
                if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
                    cantidad_producto = int(cantidad_producto)
                    break
                else:
                    print("Opcion Invalida. Intente de nuevo")
                    
            agregar_producto(nombre_producto,precio_producto,cantidad_producto)
            
            while True:
                salir = input("\n¿Quieres salir agregar mas productos? 1 (si) o 2 (no) \n")
                if salir.isdigit() == False:
                    print("Opcion invalida. Intenta de nuevo")
                elif int(salir) != 1 and int(salir) != 2:
                    print("Opcion invalida. Intenta de nuevo")
                else:
                    break
            if int(salir) == 2:
                break
        mostrar_inventario(inventario)
        
    case "2":
        print("\n-------------Buscar Producto-------------\n")
        mostrar_inventario(inventario)
        
        
        
            
                

        
    