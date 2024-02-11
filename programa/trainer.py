import json
from os import system
from .datos import trainer, camper
from .valido import menuNoValid
from programa.camper import listarCamper
from programa.camper import camper

def guardar():
    print("""
        *******************
        * Guardar Trainer *
        *******************
        """)
    info = {
        "Nro Identificacion": input("Ingrese el numero de identificacion: "),
        "Nombre completo": input("Ingrese el nombre completo: "),
        "Camper": []
    }
    trainer.append(info)
    with open("programa/datosJson/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Trainer"

def buscar():
    system("clear")
    print(f"""
    *******************
    *  Buscar Trainer  *
    *******************
    """)
    codigo = input("Ingrese el Nro Identificacion del camper que deseas buscar: ")
    try:
        codTrainer = next(index for index, camp in enumerate(trainer) if camp.get("Nro Identificacion") == codigo)
        print(f"""
    ____________________________
    Nro Identificacion: {trainer[codTrainer].get('Nro Identificacion')}
    Nombre completo: {trainer[codTrainer].get('Nombre completo')}
    ____________________________
        """)
    except StopIteration:
                print("ERROR. no se encuentra ese codigo")
    return "El camper esta disponible"

def listarTrainer():
    system("clear")
    with open("programa/datosJson/trainer.json") as f:
        traienrss = json.loads(f.read())
        f.close()
    for trainers in traienrss:
        printTrainer(trainers)

def printTrainer(trainer):
    print(f"""
            ----------------TRAINER-------------
            Nro Identificacion: {trainer["Nro Identificacion"]}
            Nombre Completo: {trainer["Nombre completo"]}
            -----------------------------------
              """)

def asignarCamper():
    with open("programa/datosJson/trainer.json", "r") as f:
        trainer = json.loads(f.read())
        f.close()
        listarTrainer()
    codtra = input("Nro Identificacion de trainer: ")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        f.close()
        listarCamper()
    while True:
        codcamp = input("Nro Identificacion de camper: ")
        for trainers in trainer:
            if trainers.get("Nro Identificacion") == codtra:
                for campers in camper:
                    if campers.get("Nro Identificacion") == codcamp:
                        trainer["Camper"].append(campers)
        with open("programa/datosJson/trainer.json", "w") as f:
            trainer = json.dumps(trainer, indent=4)
            f.write(trainer)
            f.close()
        opc = int(input("Quieres asigar otro camper?\n1.Si\n2.No\n "))
        if opc == 1:
            asignarCamper()
        elif opc == 2:
            system("clear")
            print("Camper asignado correctamente")
            break
        

def asignarRuta():
    print()

def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -            MENU TRAINER               -
    -----------------------------------------
    -     1. Guardar Trainer                -
    -     2. Buscar Trainer                 -
    -     3. Agregar Camper a Trainer       -
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
                guardar()
            case 2:
                system("clear")
                listarTrainer()
            case 3:
                system("clear")
                asignarCamper()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)