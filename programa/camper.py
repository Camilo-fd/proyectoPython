import json
from os import system
from .datos import camper
from .valido import menuNoValid

def save():
    info = {
        "Nro Identificacion": int(input("Ingrese su numero de identificacion: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido: "),
        "Direccion": input("Ingrese la direccion: "),
        "Acudiente": input("Ingrese su acudiente: "),
        "Estado": "Pre inscrito"
    }
    camper.append(info)
    with open("programa/datosJson/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Camper"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar Camper")
        print("\t0. Salir")
        opc = int(input())
        match(opc):
            case 1:
                system("clear")
                save()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)