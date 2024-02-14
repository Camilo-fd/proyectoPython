import json
from os import system
from .datos import matriculas
from programa.ruta import listarRuta
from programa.salasEntrenamiento import listarsalasEntrenamiento
from programa.trainer import listarTrainer
from programa.camper import listarCamper
from programa.horario import prinHorario

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
        "lisHorario": prinHorario(),
        "Codigo Horario": input("Codigo Horario: ")
    }
    matriculas.append(info)
    with open("programa/datosJson/matriculas.json", "w") as f:
        data = json.dumps(matriculas, indent=4)
        f.write(data)
        f.close()

def printAsignaciones():
    with open("programa/datosJson/matriculas.json", "r") as f:
        matriculas = json.loads(f.read())
        for matricula in matriculas:
            print("\033[92m----------------MATRICULA-------------")
            print(f"Codigo Rut: {matricula['Codigo Ruta']}")
            print(f"Codigo Sala: {matricula['Codigo Sala']}")
            print(f"Nro Identificacion Trainer: {matricula['Nro Identificacion Trainer']}")
            print(f"Nro Identificacion Camper: {matricula['Nro Identificacion Camper']}")
            print(f"Fecha Inicio: {matricula['Fecha Inicio']}")
            print(f"Fecha Final: {matricula['Fecha Final']}")
            print(f"Codigo Horario: {matricula['Codigo Horario']}")
            print("--------------------------------\033[92m")
            
def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -             MENU Matriculas           -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. asignaciones                   -
    -     2. listar asignaciones            -
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
            case 2:
                printAsignaciones()
            case 0:
                bandera = False