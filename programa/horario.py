from .datos import horario
import json
from os import system
from programa.valido import menuNoValid

def guardarhorarios():
    print(f"""\033[92m
    *********************
    *  Guardar Horario  *
    *********************
    \033[92m""")
    info = {
    "Nombre Jornada": input("Nombre Jornada: "),
    "Codigo": input("Codigo: "),
    "Hora": input("Hora: ")
}
    horario.append(info)
    with open("programa/datosJson/horario.json", "w") as f:
        data = json.dumps(horario, indent=4)
        f.write(data)
        f.close()

def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -            MENU HORARIO               -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Guardar horario                -
    -     0. Salir                          -
    -----------------------------------------
\033[94m""")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            case 1:
                guardarhorarios()
            case 0:
                bandera = False
            case _:
                menuNoValid(opc)