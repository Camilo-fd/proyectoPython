import json
from os import system
from programa.camper import listarCamper
from programa.trainer import listarTrainer
from programa.ruta import listarRuta, listadoCamper
from .datos import salasEntrenamiento

def ingresarSalas():
    info = {
        "Nombre Sala": input("Nombre Sala: "),
        "Codigo": input("Codigo: "),
        "Capacidad Maxima": input("Capacidad: "),
        "Ruta": [],
        "Camper": [],
        "Trainer": []
    }
    salasEntrenamiento.append(info)
    with open("programa/datosJson/salasEntrenamiento.json", "w") as f:
        data = json.dumps(salasEntrenamiento, indent=4)
        f.write(data)
        f.close()

def asigarRuta():
    with open("programa/datosJson/ruta.json", "r") as f:
        ruta = json.loads(f.read())
        listarRuta()
    codRuta = input("Codigo de la ruta: ")
    with open("programa/datosJson/salasEntrenamiento.json", "r") as f:
        salasEntrenamiento = json.loads(f.read())
        listarsalasEntrenamiento()
    bandera = True
    while (bandera):
        codSala = input("Codigo Salas Entrenamiento: ")
        for rutas in ruta:
            if rutas.get("Codigo") == codRuta:
                for salas in salasEntrenamiento:
                    if salas.get("Codigo") == codSala:
                            salas["Ruta"].append(rutas)
                            bandera = False
        with open("programa/datosJson/salasEntrenamiento.json", "w") as f:
            data = json.dumps(salasEntrenamiento, indent=4)
            f.write(data)
            f.close() 

def asignarCamper(): 
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        listarCamper()
    codCamper = input("Nro Identificacion del camper: ")
    with open("programa/datosJson/salasEntrenamiento.json", "r") as f:
        salasEntrenamiento = json.loads(f.read())
        listarsalasEntrenamiento()
    bandera = True
    while (bandera):
        codSala = input("Codigo Salas Entrenamiento: ")
        for campers in camper:
            if campers.get("Nro Identificacion") == codCamper:
                for salas in salasEntrenamiento:
                    if salas.get("Codigo") == codSala:
                            salas["Camper"].append(campers)
                            bandera = False
        with open("programa/datosJson/salasEntrenamiento.json", "w") as f:
            data = json.dumps(salasEntrenamiento, indent=4)
            f.write(data)
            f.close()

def asignarTrainer(): 
    with open("programa/datosJson/trainer.json", "r") as f:
        trainer = json.loads(f.read())
        listarTrainer()
    codTrainer = input("Nro Identificacion del trainer: ")
    with open("programa/datosJson/salasEntrenamiento.json", "r") as f:
        salasEntrenamiento = json.loads(f.read())
        listarsalasEntrenamiento()
    bandera = True
    while (bandera):
        codSala = input("Codigo Salas Entrenamiento: ")
        for trainers in trainer:
            if trainer.get("Nro Identificacion") == codTrainer:
                for salas in salasEntrenamiento:
                    if salas.get("Codigo") == codSala:
                            salas["Trainer"].append(trainers)
                            bandera = False
        with open("programa/datosJson/salasEntrenamiento.json", "w") as f:
            data = json.dumps(salasEntrenamiento, indent=4)
            f.write(data)
            f.close()

def listarsalasEntrenamiento():
    with open("programa/datosJson/salasEntrenamiento.json") as f:
        salasEntrenamiento = json.loads(f.read())
        f.close()
    for salas in salasEntrenamiento:
        printsalasEntrenamiento(salas)

def printsalasEntrenamiento(salasEntrenamiento): 
    print(f"""
            -------------Salas Entrenamiento-------------
            Nombre Sala: {salasEntrenamiento["Nombre Sala"]}
            Codigo: {salasEntrenamiento["Codigo"]}
            Capacidad Maxima: {salasEntrenamiento["Capacidad Maxima"]}
            Ruta: {salasEntrenamiento["Ruta"]}
            Camper: {listadoCamper(salasEntrenamiento)}
            ---------------------------------------------
              """)

def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -       MENU SALAS ENTRENAMIENTO        -
    -----------------------------------------
    -     1. Añadir Sala                    -
    -     2. Buscar Sala Entrenamiento      -
    -     3. Asignar Camper                 -
    -     4. Asignar Ruta                   -
    -     5. Asignar Trainer                -
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
                ingresarSalas()
            case 2:
                system("clear")
                listarsalasEntrenamiento()
            case 3:
                system("clear")
                asignarCamper()
            case 4:
                system("clear")
                asigarRuta()
            case 5:
                system("clear")
                asignarTrainer()
            case 0:
                bandera = False