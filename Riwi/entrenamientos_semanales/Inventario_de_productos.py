import sys
inventario = {
    'miguel' : {'Precio': 4000 , 'Cantidad' : 12}
}

def agregar_producto(nombre,precio,cantidad):
    detalles_producto = {'Precio':float(precio) , 'Cantidad' : cantidad}
    inventario[nombre] = detalles_producto

def mostrar_inventario(inventario):
    print("\n---------------Mostrar productos----------------")
    for nombre, detalle in inventario.items():
        print(f"Nombre: {nombre} -- Precio: {detalle['Precio']} -- Cantidad: {detalle['Cantidad']}")
    print("------------------------------------------------\n")

def buscar_producto(nombre_buscar):
    if nombre_buscar in inventario:
        print(f"\nBusqueda realizada con exito")
        print("---------------------------------------------------")
        print(f"Nombre: {nombre_buscar} -- Precio: {inventario[nombre_buscar]['Precio']} -- Cantidad: {inventario[nombre_buscar]['Cantidad']} ")
        print("---------------------------------------------------")
    else:
        print("El producto no se encuentra en el inventario")
    

def editar_precio(nombre_editar):
    if nombre_editar in inventario:
        print("\n---------------------------------------------------")
        print(f"Nombre: {nombre_editar} -- Precio: {inventario[nombre_editar]['Precio']} ")
        print("---------------------------------------------------")
        while True:
            precio_editar = input("Digita el nuevo precio para este producto: ")
            if precio_editar.isdigit() and float(precio_editar) > 0:
                precio_editar = float(precio_editar)
                break
            else:
                print("Opcion Invalida. Intente de nuevo")

        inventario[nombre_editar]['Precio'] = precio_editar

def eliminar_producto(producto_eliminar):
    if producto_eliminar in inventario:
        del inventario[producto_eliminar]
        print("Producto eliminado con exito")
    else: 
        print("Este producto no se encuentra en el inventario")


            
print("╔═════════════════════════════════════════════════════════════╗") 
print("║                     INVENTARIO DE PRODUCTOS                 ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

while True:
    print("Opciones disponibles: ")
    print("\n(1).Añadir productos \n(2).Consultar productos \n(3).Actualizar precio \n(4).Eliminar producto \n(5).Mostrar inventario \n(6).Salir del programa\n") 


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
                print("\n---------------Agregar Producto---------------\n")
                
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
                    salir = input("\n¿Quieres agregar mas productos? 1 (si) o 2 (no): ")
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
            print("\n-----------------Buscar Producto----------------\n")
            while True: 

                while True:
                    nombre_buscar = input("Ingrese por favor el nombre del producto: ")
                    if nombre_buscar.replace(" ", "").isalpha():
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo ")

                buscar_producto(nombre_buscar)
                
                
                while True:
                    salir = input("\n¿Quieres buscar mas productos? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    break

        case "3":
            print("\n-----------------Actualizar Precio----------------\n")
            while True:
                while True:
                    nombre_editar = input("Ingrese por favor el nombre del producto: ")
                    if nombre_editar.replace(" ", "").isalpha():
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo ")

                
                    
                editar_precio(nombre_editar)
                    

                while True:
                    salir = input("\n¿Quieres actualizar el precio de mas productos? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    break
        case "4":
            print("\n-----------------Eliminar Producto----------------\n")
            while True:
                while True:
                    producto_eliminar = input("Ingrese por favor el nombre del producto: ")
                    if producto_eliminar.replace(" ", "").isalpha():
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo ")

                eliminar_producto(producto_eliminar)
                    
                while True:
                    salir = input("\n¿Quieres eliminar mas productos? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    break
        case "5":
            print()
        
        case "6":
            print("Fin de programa")
            break
            
        
        
        
            
                

        
    
