import json
from os import system
from .valido import menuNoValid

def camperInscrito():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Inscrito":
                print(f"Nro Identificacion: {campers['Nro Identificacion']}")
                print(f"Nombre: {campers['Nombre']}")
                print(f"Apellido: {campers['Apellido']}")
                print(f"Direccion: {campers['Direccion']}")
                print(f"Telefonos: {campers['Telefonos']}")
                print(f"Acudiente: {campers['Acudiente']}")
                print(f"Estado: {campers['Estado']}")
                print(f"Nota: {campers['Nota']}")
                print(f"Nota Modulo: {campers['Nota Modulo']}")
                # print(json.dumps(campers, indent=4))

def camperAprovado():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Aprovado":
                # print(campers)
                # print(f"Nro Identificacion: {campers['Nro Identificacion']}")
                # print(f"Nombre: {campers['Nombre']}")
                # print(f"Apellido: {campers['Apellido']}")
                # print(f"Direccion: {campers['Direccion']}")
                # print(f"Telefonos: {campers['Telefonos']}")
                # print(f"Acudiente: {campers['Acudiente']}")
                # print(f"Estado: {campers['Estado']}")
                # print(f"Nota: {campers['Nota']}")
                # print(f"Nota Modulo: {campers['Nota Modulo']}")
                print(json.dumps(campers, indent=4))

def mostraTrainer():
    with open("programa/datosJson/trainer.json", "r") as f:
        trainer = json.loads(f.read())
        # print(trainer)
        print(json.dumps(trainer, indent=4))

def camperBajoriesgo():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "En Riesgo":
                # print(campers)
                print(json.dumps(campers, indent=4))

def listarCamperTrainerRuta():
    with open("programa/datosJson/ruta.json", "r") as f:
        ruta = json.loads(f.read())
    codRuta = input("Codigo Ruta: ")
    for rutas in ruta:
        if rutas.get("Codigo") == codRuta:
            for campers in rutas["Camper"]:
                # print(campers)
                print(json.dumps(campers, indent=4))
            for trainers in rutas["Trainer"]:
                # print(trainers)
                print(json.dumps(trainers, indent=4))

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
    -     4. Listar Camper En Riesgo         -
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
            case 4:
                system("clear")
                camperBajoriesgo()
            case 5:
                listarCamperTrainerRuta()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)