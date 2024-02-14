import json
from os import system
from .datos import matriculas
from programa.ruta import listarRuta
from programa.salasEntrenamiento import listarsalasEntrenamiento
from programa.trainer import listarTrainer
from programa.camper import listarCamper

def asignaciones():
    print(f"""\033[92m
    ********************
    *   Asignaciones   *
    ********************
    \033[92m""")
    info = {
        "lisRuta": listarRuta(),
        "Codigo Ruta": input("Codigo Ruta: "),
        "lisSala": listarsalasEntrenamiento(),
        "Codigo Sala": input("Codigo Sala: "),
        "lisTrainer": listarTrainer(),
        "Nro Identificacion Trainer": input("Nro Identificacion Trainer: "),
        "lisCamper": listarCamper(),
        "Nro Identificacion Camper": input("Nro Identificacion Camper: "),
        "Fecha Inicio": input("Fecha Inicio: "),
        "Fecha Final": input("Fecha Final: "),
        "Codigo Horario": input("Codigo Horario: ")
    }
    matriculas.append(info)
    with open("programa/datosJson/matriculas.json", "w") as f:
        data = json.loads(matriculas, ident=4)
        f.write(data)
        f.close()

def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -             MENU Matriculas           -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. asignaciones                   -
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
                system("clear")
                asignaciones()