import json
from .datos import modulo
from os import system

def crear():
    info = {
        "Codigo": int(input("Codigo: ")),
        "Nombre Modulo": input("Nombre Modulo: "),
        "Prioridad": input("Prioridad: "),
        "Temarios": []
        
    }
    for x in range(int(input("Numero de temarios: "))):
        info["Temario"] = input("Nombre temario:")
        info["Temarios"].append({"Temario": info["Temario"]})

    modulo.append(info)
    with open("programa/datosJson/modulo.json", "w") as f:
        datos = json.dumps(modulo, indent=4)
        f.write(datos)
        f.close()
        system("clear")

def leermodulo():
    with open("programa/datosJson/modulo.json", "r") as f:
        return json.loads(f.read())
    
def menu():
    bandera = True
    while (bandera):
        print("\t1. Crear Modulo")
        print("\t0. Salir Modulo")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            case 1:
                system("clear")
                crear()
            case 0:
                system("clear")
                bandera = False