movimientos = {}
id_movimiento = 1
saldo = 0
while_continuar = True
print("----------cajero automatico----------")

while while_continuar:
    print("\nOpciones disponibles: ")
    print("\n(1).Depositar dinero. \n(2).Retirar dinero. \n(3).Historial de movimientos. \n(4).Salir del programa")

    while True:
        opcion_menu = input("Ingresa una opcion del menu por favor: ")
        if opcion_menu.isdigit():
            break
        else: 
            print("Opcion invalida. Intenta de nuevo")
                
    while True:
        match opcion_menu:
            
            case "1": 
                print("----------Depositar dinero----------")
                while True:
                    deposito = input("Ingrese el monto total a depositar: ")
                    if float(deposito) and deposito.isdigit > 0:
                        print("Monto agregado con exito")
                        break
                    else:
                        print("Monto inalido. Intenta de nuevo")
                saldo += float(deposito)
                movimientos[id_movimiento] = deposito
                id_movimiento += 1
                print(f"deposito realizado con exito, saldo actual: {deposito}")    
                break
                
            case "2": 
                print("----------Retirar dinero----------")
                while True:
                    retiro = input("Ingrese el monto total a retirar: ")
                    if float(retiro) and retiro.isdigit > 0:
                        print("Monto agregado con exito")
                        break
                    else:
                        print("Monto inalido. Intenta de nuevo")
                        
                if float(retiro) > saldo:
                    print("Fondos insuficientes. Retiro invalido")
                else:
                    saldo -= float(retiro)
                    movimientos[id_movimiento] = f"-{retiro}"
                    id_movimiento += 1
                    print("Depositoo realizado con exito")
                break
                    
                    
            case "3":
                print("----------Historial de movimientos----------")
                print(movimientos)
                break
                
                
            case "4":
                print("----------Fin del programa----------")
                while_continuar = False
                break
                
    
        
        
        
