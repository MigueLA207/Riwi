licencia = input("¿Tiene usted licencia de conducir? (si/no): ")
casco = input("¿Lleva usted casco? (si/no): ")

if licencia != "si" or casco != "si":
    print("No puedes conducir")
else:
    print("Puedes conducir con seguridad")
