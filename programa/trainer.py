import json
from os import system
from .datos import trainer
from .valido import menuNoValid

def guardar():
    info = {
        "Nro Identificacion": input("Ingrese el numero de identificacion: "),
        "Nombre completo": input("Ingrese el nombre completo: ")
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
    *  Lista Trainer  *
    *******************
    """)
    for i,val in enumerate(trainer):
        print(f"""
    ____________________________
    Codigo: {i}
    Nro Identificacion: {val.get('Nro Identificacion')}
    Nombre completo: {val.get('Nombre completo')}
    ____________________________
        """)
    return "El camper esta disponible"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del trainer")
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t0. Atras")
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
                buscar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)