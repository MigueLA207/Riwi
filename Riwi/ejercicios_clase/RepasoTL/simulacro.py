
students = {
    1001 : {'name':'Miguel Angel Arias Marin','age': 17,'note': 4.5 },
    1002 : {'name':'Juan Esteban Sepulveda','age': 18,'note': 4 },
    1003 : {'name':'Carlos Marin Herrera','age': 16,'note': 3.6 },
    1004 : {'name':'Juan Fernando Puerta','age': 17,'note': 2.8 },
    1005 : {'name':'Valentina Arteaga Rendon','age': 15,'note': 5 }
}

def show_students(students):
    print("\n-------------Lista de estudiantes-------------")
    for id, details in students.items():
        print(f"ID: {id} -- Nombre: {details['name']} -- Edad: {details['age']} -- Nota: {details['note']}")
    print("----------------------------------------\n")

def add_student(student_id,student_name,student_age,student_note):
    student_details = {'name':student_name , 'age' : student_age , 'note' : student_note}
    students[student_id] = student_details

def search_name(search):
        for id, details in students.items():
            if search == details['name']:
                return True
        return False

def edit_data(edit,edit_student):
    if edit == 1:
        print(f"Estudiante a editar: {students[edit_student]}")
    else:
        print("En proceso")




print("╔═════════════════════════════════════════════════════════════╗") 
print("║                     GESTION DE ESTUDIANTES                  ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

while True:
    print("\nOpciones disponibles: ")
    print("\n(1).Agregar estudiantes. \n(2).Buscar estudiante. \n(3).Actualizar informacion de estudiante. \n(4).Eliminar estudiante. \n(5).Calcular el promedio estudiantil. \n(6).Estudiantes desaprovados.") 

    while True:
        menu_option = input("\nInserta una opcion del menu: ")
        if menu_option.isdigit() and 1 <= int(menu_option) <= 5:
            break
        else: 
            print("Opcion invalida. Intenta de nuevo")

    match menu_option:
        case "1":
            while True: 
                print("\n-------------Agregar estudiante-------------\n")
                
                while True:
                    student_id = input("Ingrese el numero del documento de identidad: ")
                    if student_id.isdigit() and int(student_id) > 0 and int(student_id) not in students:
                        student_id = int(student_id)
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo")

                while True:
                    student_name = input("Ingrese por favor el nombre completo del estudiante: ")
                    if student_name.replace(" ", "").isalpha():
                        student_name.title()
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo ")
                        
                while True:
                    student_age = input("Ingrese por favor la edad del estudiante: ")
                    if student_age.isdigit() and int(student_age) > 0:
                        student_age = int(student_age)
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo")
                
                while True:
                    student_note = input("Ingrese por favor la nota del estudiante, si es decimal con coma(.): ")
                    if 1 <= float(student_note) <= 5:
                        student_note = float(student_note)
                        break
                    else:
                        print("Opcion Invalida. Intente de nuevo")
                
                        
                add_student(student_id,student_name,student_age,student_note)
                
                
                while True:
                    salir = input("\n¿Quieres agregar mas estudiantes? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    break

        case "2": 
            while True: 
                leave = True
                print("\n-------------Buscar estudiante-------------\n")
                
                search = input("Ingrese por favor el documento de identidad o el nombre del estudiante: ")

                if search.isdigit():
                    search_id = int(search)
                else:
                    search_id = search

                if search_name(search) == True or search_id in students:
                    print("El estudiante si se encuentra en la base de datos")

                else:
                    print("El estudiante no se encuentra en la base de datos")

                
                while True:
                    salir = input("\n¿Deseas intentar otra vez? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    print("----------------------------------------\n")
                    break
        case "3":
            while True: 
                leave = True
                print("\n-------------Editar estudiante-------------\n")

                show_students(students)
            
                edit_student = input("Ingrese por favor el documento de identidad:  ")

                if edit_student.isdigit():
                    if int(edit_student) in students:
                        edit_student = int(edit_student)
                        print("\n¿Que dato deseas editar?")
                        print("\n(1).Edad \n(2)Nota")
                        while True:
                            edit = input("Ingrese opcion: ")
                            if edit.isdigit() and 1 <= int(edit) <= 2:
                                edit = int(edit)
                                edit_data(edit,edit_student)
                    else:
                        print(f"El documento {edit_student}. Intenta de nuevo")

                else:
                    print("Opcion invalida. Intenta de nuevo")

                
                
                while True:
                    salir = input("\n¿Deseas intentar otra vez? 1 (si) o 2 (no) \n")
                    if salir.isdigit() == False:
                        print("Opcion invalida. Intenta de nuevo")
                    elif int(salir) != 1 and int(salir) != 2:
                        print("Opcion invalida. Intenta de nuevo")
                    else:
                        break
                if int(salir) == 2:
                    print("----------------------------------------\n")
                    break
        