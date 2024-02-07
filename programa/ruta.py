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
        

def asigarmodulo():
    with open("programa/datosJson/ruta.json", "r") as f:
                rutas = json.loads(f.read())
                f.close()
    print(rutas)
    codruta = int(input("Codigo de ruta: "))
    print(rutas[codruta])
    with open("programa/datosJson/modulo.json", "r") as f:
                modulos = json.loads(f.read())
                f.close()
    print(modulos)
    while True:
        codmod = int(input("Codigo de modulo: "))
        print(modulos[codmod])
        rutas[codruta]["Modulo"].append(modulos[codmod])
        with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(rutas, indent=4)
            f.write(rutas)
            f.close()
        opc = int(input())
        if opc == 1:
            asigarmodulo()
        break


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
                asigarmodulo()
