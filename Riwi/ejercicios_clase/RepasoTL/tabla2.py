from tabulate import tabulate

# Datos de usuarios
usuarios = {
    "1": {
        "nombre": "Daniel",
        "apellido": "Herrera",
        "contacto": {
            "correo": "garyford@gmail.com",
            "telefono": "001-512-801-0651x67779",
            "direccion": {
                "calle": "178 Walker Island Suite 840",
                "ciudad": "Gonzalezmouth",
                "estado": "Michigan",
                "codigo_postal": "92488",
                "pais": "Bermuda"
            }
        },
        "perfil": {
            "username": "bradley18",
            "fecha_nacimiento": "1987-07-15",
            "genero": "Masculino",
            "ocupacion": "Financial planner"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/mistytaylor",
            "linkedin": "https://linkedin.com/in/nancythomas",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": True,
            "temas_interes": ["arte", "moda", "tecnología"]
        }
    },
    "2": {
        "nombre": "Joseph",
        "apellido": "Sullivan",
        "contacto": {
            "correo": "grussell@hotmail.com",
            "telefono": "006-305-4158x3659",
            "direccion": {
                "calle": "9638 Hawkins Crossing Apt. 914",
                "ciudad": "Robertchester",
                "estado": "Illinois",
                "codigo_postal": "28682",
                "pais": "Ethiopia"
            }
        },
        "perfil": {
            "username": "kennethtaylor",
            "fecha_nacimiento": "1981-03-26",
            "genero": "Otro",
            "ocupacion": "Clinical psychologist"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/claire15",
            "linkedin": "",
            "instagram": "https://instagram.com/kellycooper"
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": False,
            "temas_interes": ["deportes", "arte", "viajes"]
        }
    },
    "3": {
        "nombre": "Kristina",
        "apellido": "Bradley",
        "contacto": {
            "correo": "mark58@hotmail.com",
            "telefono": "771-464-1767",
            "direccion": {
                "calle": "9396 Martin Bridge Apt. 544",
                "ciudad": "South Ryan",
                "estado": "Iowa",
                "codigo_postal": "41958",
                "pais": "Philippines"
            }
        },
        "perfil": {
            "username": "christine51",
            "fecha_nacimiento": "1966-09-21",
            "genero": "Femenino",
            "ocupacion": "Restaurant manager, fast food"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/dickersonjustin",
            "linkedin": "https://linkedin.com/in/michaela78",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["cocina", "tecnología", "viajes"]
        }
    },
    "4": {
        "nombre": "Monica",
        "apellido": "Molina",
        "contacto": {
            "correo": "daniel59@yahoo.com",
            "telefono": "(925)185-9544x03157",
            "direccion": {
                "calle": "53484 Garrett Wall",
                "ciudad": "East Sherri",
                "estado": "Washington",
                "codigo_postal": "81748",
                "pais": "Syrian Arab Republic"
            }
        },
        "perfil": {
            "username": "kayla97",
            "fecha_nacimiento": "1987-11-19",
            "genero": "Femenino",
            "ocupacion": "Company secretary"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/rgomez",
            "linkedin": "",
            "instagram": "https://instagram.com/sarah44"
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["viajes", "deportes", "tecnología"]
        }
    },
    "5": {
        "nombre": "Angela",
        "apellido": "House",
        "contacto": {
            "correo": "pwaters@dixon.biz",
            "telefono": "(616)639-1141",
            "direccion": {
                "calle": "8264 Morgan Lights",
                "ciudad": "Dianetown",
                "estado": "North Dakota",
                "codigo_postal": "64546",
                "pais": "Bolivia"
            }
        },
        "perfil": {
            "username": "randy13",
            "fecha_nacimiento": "2006-02-20",
            "genero": "Masculino",
            "ocupacion": "Airline pilot"
        },
        "redes_sociales": {
            "twitter": "",
            "linkedin": "https://linkedin.com/in/watkinsjessica",
            "instagram": "https://instagram.com/longlaura"
        },
        "preferencias": {
            "idioma": "Inglés",
            "newsletter": False,
            "temas_interes": ["moda", "arte", "cocina"]
        }
    }
}

# Función para acortar texto largo
def acortar_texto(texto, longitud=15):
    if not texto:
        return ""
    if len(str(texto)) <= longitud:
        return texto
    return str(texto)[:longitud-3] + "..."

# Método 1: Tablas separadas por secciones - más legible
def mostrar_tablas_separadas():
    # Tabla 1: Información personal básica
    filas_basicas = []
    for id, usuario in usuarios.items():
        filas_basicas.append([
            id,
            usuario["nombre"],
            usuario["apellido"],
            acortar_texto(usuario["perfil"]["username"], 15),
            usuario["perfil"]["fecha_nacimiento"],
            usuario["perfil"]["genero"],
            acortar_texto(usuario["perfil"]["ocupacion"], 20)
        ])
    
    print("\n=== INFORMACIÓN PERSONAL ===")
    print(tabulate(
        filas_basicas,
        headers=["ID", "Nombre", "Apellido", "Username", "Fecha Nac.", "Género", "Ocupación"],
        tablefmt="grid"
    ))
    
    # Tabla 2: Información de contacto
    filas_contacto = []
    for id, usuario in usuarios.items():
        dir = usuario["contacto"]["direccion"]
        filas_contacto.append([
            id,
            usuario["nombre"] + " " + usuario["apellido"],
            acortar_texto(usuario["contacto"]["correo"], 20),
            acortar_texto(usuario["contacto"]["telefono"], 15),
            acortar_texto(dir["calle"], 25),
            acortar_texto(dir["ciudad"], 15),
            acortar_texto(dir["estado"], 12),
            dir["codigo_postal"],
            acortar_texto(dir["pais"], 12)
        ])
    
    print("\n=== INFORMACIÓN DE CONTACTO ===")
    print(tabulate(
        filas_contacto,
        headers=["ID", "Nombre", "Correo", "Teléfono", "Calle", "Ciudad", "Estado", "C.P.", "País"],
        tablefmt="grid"
    ))
    
    # Tabla 3: Redes sociales y preferencias
    filas_redes = []
    for id, usuario in usuarios.items():
        redes = usuario["redes_sociales"]
        prefs = usuario["preferencias"]
        filas_redes.append([
            id,
            usuario["nombre"] + " " + usuario["apellido"],
            acortar_texto(redes["twitter"], 20) or "-",
            acortar_texto(redes["linkedin"], 20) or "-",
            acortar_texto(redes["instagram"], 20) or "-",
            prefs["idioma"],
            "Sí" if prefs["newsletter"] else "No",
            ", ".join(prefs["temas_interes"])
        ])
    
    print("\n=== REDES SOCIALES Y PREFERENCIAS ===")
    print(tabulate(
        filas_redes,
        headers=["ID", "Nombre", "Twitter", "LinkedIn", "Instagram", "Idioma", "Newsletter", "Intereses"],
        tablefmt="grid"
    ))

# Método 2: Una tabla compacta con información esencial
def mostrar_tabla_compacta():
    filas = []
    for id, usuario in usuarios.items():
        filas.append([
            id,
            usuario["nombre"] + " " + usuario["apellido"],
            acortar_texto(usuario["contacto"]["correo"], 20),
            acortar_texto(usuario["contacto"]["telefono"], 15),
            usuario["perfil"]["fecha_nacimiento"],
            usuario["perfil"]["genero"],
            acortar_texto(usuario["perfil"]["ocupacion"], 15),
            usuario["preferencias"]["idioma"],
            "Sí" if usuario["preferencias"]["newsletter"] else "No",
            ", ".join(usuario["preferencias"]["temas_interes"])
        ])
    
    print("\n=== TABLA DE USUARIOS (COMPACTA) ===")
    print(tabulate(
        filas,
        headers=["ID", "Nombre", "Correo", "Teléfono", "Fecha Nac.", "Género", "Ocupación", "Idioma", "News", "Intereses"],
        tablefmt="grid"
    ))

# Ejecuta ambos métodos de visualización
print("VISUALIZACIÓN DE DATOS DE USUARIOS")
print("=" * 40)

# Elegir uno de los dos métodos (o descomentar ambos para ver las dos opciones)
mostrar_tablas_separadas()
#mostrar_tabla_compacta()