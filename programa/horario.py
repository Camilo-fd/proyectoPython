from .datos import horario
import json
from os import system
from programa.valido import menuNoValid

def guardarhorarios():
    info = {
    "Nombre Jornada": input("Nombre Jornada: "),
    "Codigo": int(input("Codigo: ")),
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
        print("""
        *****************
        * Menu Horarios *
        *****************
        """)
        print("1. Guardar horario")
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