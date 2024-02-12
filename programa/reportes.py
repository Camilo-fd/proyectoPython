import json
from os import system
from .valido import menuNoValid

def camperInscrito():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Inscrito":
                print(campers)

def camperAprovado():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Aprovado":
                print(campers)

def mostraTrainer():
    with open("programa/datosJson/trainer.json", "r") as f:
        trainer = json.loads(f.read())
        print(trainer)


def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -             MENU Reportes             -
    -----------------------------------------
    -     1. Listar Camper Inscritos        -
    -     2. Listar Camper Aprovados        -
    -     3. Listar Trainer                 -
    -     4. Listar Camper Bajo Rendimiento -
    -     5. Listar Camper y Trainer        -
    -          asociados a una ruta         -
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
                system("clear")
                camperInscrito()
            case 2:
                system("clear")
                camperAprovado()
            case 3:
                system("clear")
                mostraTrainer()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)