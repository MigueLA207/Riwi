edad = int(input("Digite su edad por favor: "))
if edad < 13:
    print("Eres un nino")
elif edad >= 13 and edad < 18:
    print("Eres un adolecente")
elif edad >= 18 and edad <60:
    print("Eres un adulto ")
elif edad >=60:
    print("Eres un anciano")
else:
    print("Dato no valido")
    