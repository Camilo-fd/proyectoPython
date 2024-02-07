import json
from os import system
from .datos import ruta, modulo
from programa.modulo import modulo

def ingresar():
    info = {
        "Codigo": int(input("Codigo: ")),
        "Nombre Ruta": input("Nombre de la ruta: "),
        "Modulo": []
    }

    ruta.append(info)
    with open("programa/datosJson/ruta.json", "w") as f:
        data = json.dumps(ruta, indent=4)
        f.write(data)
        f.close()
        system("clear")
    print("                               ")
    print("Ruta registrada correctamente")
    print("                               ")


def editar():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************
        * Editar Ruta *
        ***************
        """)
        codigo = int(input("Ingrese el codigo de la ruta: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre Ruta: {ruta[codigo].get('Nombre Ruta')}
    Modulo: {ruta[codigo].get('Modulo')}
        """)

def asignarModulo():
    bandera = True
    while (bandera):
        print(f"""
    ******************
    *  Asigar Modulo  *
    ******************
    """)
    info = {
        "Codigo": int(input("Codigo: ")),
        "Nombre Ruta": input("Nombre de la ruta: "),
        "Modulo": []
    }
    info["Modulo"].append(info["modulo"])
    bandera = False
    return info

def menu():
    bandera = True
    while (bandera):
        print(f"""
    ******************
    *  Rutas Camper  *
    ******************
    """)
        print("\t1. Ingresar Ruta")
        print("\t2. Editar Ruta")
        print("\t3. Asiganar modulo")
        print("\t0. Salir")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            case 1:
                system("clear")
                ingresar()
            case 2:
                system("clear")
                editar()
            case 3:
                system("clear")
                asignarModulo()
