nota = float(input("Ingrese su nota por favor: "))
if nota < 5:
    print("Reprobo")
elif nota >= 5 and nota < 7:
    print("aprobado")
elif nota >= 7 and nota <=10:
    print("Sobresaliente")
else:
    print("Perdio por no saber leer")