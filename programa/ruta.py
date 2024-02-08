import json
from os import system
from .datos import ruta, modulo
from programa.modulo import modulo

def ingresar():
    while True:
        print("""
        ******************
        * Registrar Ruta *
        *******************
        """)
        codigo = input("Codigo Ruta: ")
        for modulos in modulo:
                if modulos["Codigo"] == codigo:
                    print("                                                           ")
                    print("Este codigo de ruta ya esta creado, ingrese uno diferente")
                    break
        else:
                   break
    info = {
        "Codigo": codigo,
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
        print("¿Este es el camper que deseas actualizar?")
        print("1. Si")
        print("2. No Salir")
        opc = int(input())
        if (opc == 1):
            while True:
                codigo = input("Codigo Ruta: ")
                for modulos in modulo:
                    if modulos["Codigo"] == codigo:
                        print("                                                           ")
                        print("Este codigo de ruta ya esta creado, ingrese uno diferente")
                        break
                    else:
                        break
                info = {
                    "Codigo": codigo,
                    "Nombre Ruta": input("Nombre de la ruta: "),
                    "Modulo": []
            }
                ruta.append(info)
                with open("programa/datosJson/ruta.json", "w") as f:
                    data = json.dumps(ruta, indent=4)
                    f.write(data)
                    f.close()
                    system("clear")
        elif (opc == 2):
            bandera = False
            system("clear")

def printRuta(ruta):
    print(f"""
            Codigo: {ruta["Codigo"]}
            Nombre Ruta: {ruta["Nombre Ruta"]}
            Modulos: {listado(ruta)}
              """)

def listado(ruta):
            for i in ruta["Modulo"]:
                return(f"""
                    Codigo: {i["Codigo"]}
                    Nombre Modulo: {i["Nombre Modulo"]}
                    Prioridad: {i["Prioridad"]}
                      """)
            
def asigarmodulo():
    print("""
        ******************
        * Asignar Modulo *
        ******************
        """)
    with open("programa/datosJson/ruta.json", "r") as f:
        rutas = json.loads(f.read())
        f.close()
    for ruta in rutas:
        printRuta(ruta)
    # codruta = int(input("Codigo de ruta: "))
    codruta = int(input("Codigo Ruta: "))
    for i,val in enumerate(rutas):
        if (val.get('Codigo') == codruta):
            printRuta(rutas[codruta])
    with open("programa/datosJson/modulo.json", "r") as f:
        modulos = json.loads(f.read())
        f.close()
    while True:
        codmod = int(input("Codigo de modulo: "))
        for i,val in enumerate(modulos):
            if (val.get('Codigo') == codmod):
                print(modulos[codmod])
        rutas[codruta]["Modulo"].append(modulos[codmod])
        with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(rutas, indent=4)
            f.write(rutas)
            f.close()
        opc = int(input("Quieres asigar otro modulo?\n1.Si\n2.No\n "))
        if opc == 1:
            asigarmodulo()
        elif opc == 2:
            system("clear")
            print("Modulo asignado correctamente")
            break


def menu():
    bandera = True
    while (bandera):
        print(f"""
    ******************
    *  Rutas Camper  *
    ******************
    """)
        print("\t1. Registrar Ruta")
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
