import json
from os import system
from programa.camper import listarCamper
from .datos import ruta, modulo, camper
from programa.modulo import modulo
from programa.camper import camper as campermodulo

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
        "Modulo": [],
        "Camper": []
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

def listarRuta():
    system("clear")
    print(f"""
    ******************
    *  Listar Rutas  *
    ******************
    """)

    with open("programa/datosJson/ruta.json", "r") as f:
        rutas = json.loads(f.read())
        f.close()
    for ruta in rutas:
        printRuta(ruta)
            
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

def printRuta(ruta): # IMPRIMO LA RUTA LINDO
    print(f"""
            -----------------------RUTA-----------------------
            Codigo: {ruta["Codigo"]}
            Nombre Ruta: {ruta["Nombre Ruta"]}
            Modulos:{listadoruta(ruta)}
            --------------------------------------------------
              """)

def listadoruta(ruta): # LISTO LA RUTA 
            for i in ruta["Modulo"]:
                return(f"""
                    Codigo: {i["Codigo"]}
                    Nombre Modulo: {i["Nombre Modulo"]}
                    Prioridad: {i["Prioridad"]}
                      """)
            
def printModulo(modulo): # IMPRIMO EL MODULO LINDO
    print(f"""
            ----------------MODULO-------------
            Codigo: {modulo["Codigo"]}
            Nombre Modulo: {modulo["Nombre Modulo"]}
            Prioridad: {modulo["Prioridad"]}
            Temarios: {listadomodulo(modulo)}
            -----------------------------------
              """)

def listadomodulo(modulo): # LISTO LOS TEMARIOS
    texto=""
    for i in modulo["Temarios"]:
        texto+=f'\n\t\t     {i["Temario"]} '
    return (texto)

def asigarmodulo():
    varRuta = 0
    varMod = 0
    print("""
        *************************
        * Asignar Modulo A RUTA *
        *************************
        """)
    with open("programa/datosJson/ruta.json", "r") as f:
        rutas = json.loads(f.read())
        f.close()
    for ruta in rutas:
        printRuta(ruta)
    codruta = int(input("Codigo Ruta: "))
    for i,val in enumerate(rutas):
        if (val.get('Codigo') == codruta):
            printRuta(rutas[codruta])
            varRuta = i
    with open("programa/datosJson/modulo.json", "r") as f:
        modulos = json.loads(f.read())
        f.close()
    for modulo in modulos:
        printModulo(modulo)
    while True:
        codmod = int(input("Codigo de modulo: "))
        for i,val in enumerate(modulos):
            if (val.get('Codigo') == codmod):
                print("Asignacion Exitosa")
                print("                  ")
                varMod = i
        rutas[varRuta]["Modulo"].append(modulos[varMod])
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

def asignarCamper():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
    print("""
        *************************
        * Asignar Camper a Ruta *
        *************************
        """)
    listarCamper()
    codCamper = input("Nro Identificacion del camper: ")
    listarRuta()
    codRuta = input("Codigo Ruta: ")
    for rutas in ruta:
        if rutas.get("Codigo") == codRuta:
            for campers in camper:
                if campers.get("Nro Identificacion") == codCamper:
                    rutas["Camper"].append(campers)
    with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(rutas, indent=4)
            f.write(rutas)
            f.close()

def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -              MENU RUTAS               -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Registrar Ruta                 -
    -     2. Editar Ruta                    -
    -     3. Buscar Ruta                    -
    -     4. Asignar modulo                 -
    -     5. Asignar Camper                 -
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
                ingresar()
            case 2:
                system("clear")
                editar()
            case 3:
                system("clear")
                listarRuta()
            case 4:
                system("clear")
                asigarmodulo()
            case 5:
                asignarCamper()
            case 0:
                system("clear")
                bandera = False
