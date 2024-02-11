import json
from os import system
from .datos import salasEntrenamiento

def ingresarSalas():
    info = {
        "Nombre Sala": input("Nombre Sala: "),
        "Codigo": int(input("Codigo: ")),
        "Capacidad Maxima": print("Capacidad Maxima 33")
    }
    salasEntrenamiento.append(info)
    with open("programa/datosJson/salasEntrenamiento.json", "w") as f:
        data = json.dumps(salasEntrenamiento, indent=4)
        f.write(data)
        f.close()


def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -       MENU SALAS ENTRENAMIENTO        -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Añadir Sala                    -
    -     0. Salir                          -
    -----------------------------------------
""")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            case 1:
                ingresarSalas()
            case 0:
                bandera = False