from tabulate import tabulate
from colorama import init, Fore, Style
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




# Inicializar colorama (necesario para Windows)
# Inicializa colorama
init(autoreset=True)

def colorear_encabezados(encabezados, color):
    return [color + Style.BRIGHT + h + Style.RESET_ALL for h in encabezados]

# === PERFIL DEL USUARIO ===
filas_perfil = [] 
for id_usuario, usuario in usuarios.items():
    filas_perfil.append([
        Fore.MAGENTA + id_usuario + Style.RESET_ALL,
        usuario["nombre"],
        usuario["apellido"],
        usuario["perfil"]["username"],
        usuario["perfil"]["fecha_nacimiento"],
        usuario["perfil"]["genero"],
        usuario["perfil"]["ocupacion"]
    ])

encabezados_perfil = colorear_encabezados(
    ["ID", "Nombre", "Apellido", "Username", "Fecha nac.", "Género", "Ocupación"],
    Fore.CYAN
)
print(f"\n{Fore.CYAN + Style.BRIGHT}=== PERFIL DEL USUARIO ==={Style.RESET_ALL}")
print(tabulate(filas_perfil, headers=encabezados_perfil, tablefmt="grid"))


# === INFORMACIÓN DE CONTACTO ===
filas_contacto = []
for id_usuario, usuario in usuarios.items():
    direccion = usuario["contacto"]["direccion"]
    filas_contacto.append([
        Fore.MAGENTA + id_usuario + Style.RESET_ALL,
        usuario["contacto"]["correo"],
        usuario["contacto"]["telefono"],
        direccion["calle"],
        direccion["ciudad"],
        direccion["estado"],
        direccion["codigo_postal"],
        direccion["pais"]
    ])

encabezados_contacto = colorear_encabezados(
    ["ID", "Correo", "Teléfono", "Calle", "Ciudad", "Estado", "Código postal", "País"],
    Fore.YELLOW
)
print(f"\n{Fore.YELLOW + Style.BRIGHT}=== INFORMACIÓN DE CONTACTO ==={Style.RESET_ALL}")
print(tabulate(filas_contacto, headers=encabezados_contacto, tablefmt="grid"))


# === REDES SOCIALES Y PREFERENCIAS ===
filas_preferencias = []
for id_usuario, usuario in usuarios.items():
    filas_preferencias.append([
        Fore.MAGENTA + id_usuario + Style.RESET_ALL,
        usuario["redes_sociales"]["twitter"],
        usuario["redes_sociales"]["linkedin"],
        usuario["redes_sociales"]["instagram"],
        usuario["preferencias"]["idioma"],
        "Sí" if usuario["preferencias"]["newsletter"] else "No",
        ", ".join(usuario["preferencias"]["temas_interes"])
    ])

encabezados_preferencias = colorear_encabezados(
    ["ID", "Twitter", "LinkedIn", "Instagram", "Idioma", "Newsletter", "Temas interés"],
    Fore.GREEN
)
print(f"\n{Fore.GREEN + Style.BRIGHT}=== REDES SOCIALES Y PREFERENCIAS ==={Style.RESET_ALL}")
print(tabulate(filas_preferencias, headers=encabezados_preferencias, tablefmt="grid"))

