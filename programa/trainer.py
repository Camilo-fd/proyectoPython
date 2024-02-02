import json
from os import system
from .datos import trainer
from .valido import menuNoValid

def save():
    info = {
        "Nombre": input("Ingrese el nombre del trainer: "),
        "Apellido": input("Ingrese el apellido: "),
        "Edad": int(input("Ingrese la edad: ")),
    }
    trainer.append(info)
    with open("programa/datosJson/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Trainer"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del trainer")
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1:
                save()
            # case 2:
            #     system("clear")
            #     search()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)