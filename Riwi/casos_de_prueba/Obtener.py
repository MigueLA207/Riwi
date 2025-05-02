#Diccionario
alumno = {
    'Nombre' : 'Miguel',
    'Edad' : 15,
    'grado': 6
}
#obtener valor
print(alumno.get('Nombre'))

#Valor que no existe
print(alumno.get('Apellido'))

#valor que no existe con la excepcion
print(alumno.get('Apellido','Esta clave no esta en el diccionario'))