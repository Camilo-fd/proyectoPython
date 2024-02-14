import json
from os import system
from programa.camper import listarCamper
from programa.trainer import listarTrainer
from .datos import ruta, modulo
from programa.modulo import modulo
from programa.camper import camper

def ingresar():
    while True:
        print("""\033[92m\t\t
        ******************
        * Registrar Ruta *
        ******************
        \033[92m""")
        codigo = input("Codigo Ruta: ")
        for rutas in ruta:
                if rutas["Codigo"] == codigo:
                    print("                                                           ")
                    print("Este codigo de ruta ya esta creado, ingrese uno diferente")
                    break
        else:
                   break
    info = {
        "Codigo": codigo,
        "Nombre Ruta": input("Nombre de la ruta: "),
        "Modulo": [],
        "Camper": [],
        "Trainer": []
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
        print("""\033[92m\t\t
        ***************
        * Editar Ruta *
        ***************
        \033[92m""")
        codigo = input("Ingrese el Codigo de la ruta que deseas actualizar: ")
        try:
            codRuta = next(index for index, camp in enumerate(ruta) if camp.get("Codigo") == codigo)
            print(f"""
    ________________________
    Codigo: {codigo}
    Nombre Ruta: {ruta[codRuta].get('Nombre Ruta')}
        """)
            print("¿Esta es la ruta que deseas actualizar?")
            print("1. Si")
            print("2. Salir")
            opc = int(input())
            if (opc == 1):
                    codig = input("Codigo Ruta: ")
                    for rutas in ruta:
                        if rutas["Codigo"] == codig:
                            print("                                                           ")
                            print("Este codigo de ruta ya esta creado, ingrese uno diferente")
                            break
                        else:
                            break
                    info = {
                        "Codigo": codig,
                        "Nombre Ruta": input("Nombre de la ruta: "),
                        "Modulo": [],
                        "Camper": [],
                        "Trainer": []
                }
                    ruta[codRuta] = info
                    with open("programa/datosJson/ruta.json", "w") as f:
                        data = json.dumps(ruta, indent=4)
                        f.write(data)
                        f.close()
                        system("clear")
                    bandera = False
            elif (opc == 2):
                bandera = False
                system("clear")
        except StopIteration:
                print("ERROR. no se encuentra ese codigo")

def listarRuta():
    system("clear")
    print("""\033[92m\t\t
        ***************
        * Listar Ruta *
        ***************
        \033[92m""")

    with open("programa/datosJson/ruta.json", "r") as f:
        rutas = json.loads(f.read())
        f.close()
    for ruta in rutas:
        printRuta(ruta)
            
def printRuta(ruta): # IMPRIMO LA RUTA LINDO
    print(f"""\033[92m
            -----------------------RUTA-----------------------
            Codigo: {ruta['Codigo']}
            Nombre Ruta: {ruta['Nombre Ruta']}
            Modulos:{listadoModulo(ruta)}
            --------------------------------------------------
            \033[92m""")

def printModulo(modulo): # IMPRIMO EL MODULO LINDO
    print(f"""\033[92m
            ----------------MODULO-------------
            Codigo: {modulo["Codigo"]}
            Nombre Modulo: {modulo["Nombre Modulo"]}
            Prioridad: {modulo["Prioridad"]}
            Temarios: {listadoTemarios(modulo)}
            -----------------------------------
              \033[92m""")

def listadoModulo(ruta): # LISTO EL MODULO
    tabulado = ""     
    for i in ruta['Modulo']:
        tabulado += (f"""
            \t     Codigo: {i["Codigo"]}
            \t     Nombre Modulo: {i["Nombre Modulo"]}
            \t     Prioridad: {i["Prioridad"]}
            Temarios: {listadoTemarios(i)}
                """)
    return tabulado

def listadoTemarios(modulo): # LISTO LOS TEMARIOS
    texto=""
    for i in modulo["Temarios"]:
        texto+=f'\n\t\t     {i["Temario"]} '
    return (texto)

def listadoCamper(ruta):
    for i in ruta["Camper"]:
        return(f"""\033[92m
                    Nro Identificacion: {i["Nro Identificacion"]}
                    Nombre:  {i["Nombre"]}
                    Apellido:  {i["Apellido"]}
                    Direccion:  {i["Direccion"]}
                    Telefonos:  {i["Telefonos"]}
                    Acudiente:  {i["Acudiente"]}
                    Estado:  {i["Estado"]}
                    Nota:  {i["Nota"]}
                    Nota Modulo: {i["Nota Modulo"]}
               \033[92m""")

def asigarmodulo():
    varRuta = 0
    varMod = 0
    print("""\033[92m
        *************************
        * Asignar Modulo A RUTA *
        *************************
        \033[92m""")
    with open("programa/datosJson/ruta.json", "r") as f:
        rutas = json.loads(f.read())
        f.close()
    for ruta in rutas:
        printRuta(ruta)
    codruta = input("Codigo Ruta: ")
    for i,val in enumerate(rutas):
        if (val.get('Codigo') == codruta):
            varRuta = i
    with open("programa/datosJson/modulo.json", "r") as f:
        modulos = json.loads(f.read())
        f.close()
    for modulo in modulos:
        printModulo(modulo)
    while True:
        codmod = input("Codigo de modulo: ")
        for i,val in enumerate(modulos):
            if (val.get('Codigo') == codmod):
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
    print("""\033[92m
        *************************
        * Asignar Camper a Ruta *
        *************************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        listarCamper()
    codCamper = input("Nro Identificacion del camper: ")
    with open("programa/datosJson/ruta.json", "r") as f:
        ruta = json.loads(f.read())
        listarRuta()
    bandera = True
    while (bandera):
        codRuta = input("Codigo Ruta: ")
        for campers in camper:
            if campers.get("Nro Identificacion") == codCamper:
                for rutas in ruta:
                    if rutas.get("Codigo") == codRuta:
                            rutas["Camper"].append(campers)
                            bandera = False
        with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(ruta, indent=4)
            f.write(rutas)
            f.close()

def asignarTrainer(): 
    print("""\033[92m
        *************************
        * Asignar Trainer a Ruta *
        *************************
        \033[92m""")
    with open("programa/datosJson/trainer.json", "r") as f:
        trainer = json.loads(f.read())
    listarTrainer()
    codTrainer = input("Nro Identificacion del trainer: ")
    with open("programa/datosJson/ruta.json", "r") as f:
        ruta = json.loads(f.read())
        listarRuta()
    bandera = True
    while (bandera):
        codRuta = input("Codigo Ruta: ")
        for trainers in trainer:
            if trainers.get("Nro Identificacion") == codTrainer:
                for rutas in ruta:
                    if rutas.get("Codigo") == codRuta:
                            rutas["Trainer"].append(trainers)
                            bandera = False
        with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(ruta, indent=4)
            f.write(rutas)
            f.close()


def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -              MENU RUTAS               -
    -----------------------------------------
    -     1. Registrar Ruta                 -
    -     2. Editar Ruta                    -
    -     3. Buscar Ruta                    -
    -     4. Asignar modulo                 -
    -     5. Asignar Camper                 -
    -     6. Asignar Trainer                -
    -     0. Salir                          -
    -----------------------------------------
\033[94m""")
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
                system("clear")
                asignarCamper()
            case 6:
                system("clear")
                asignarTrainer()
            case 0:
                system("clear")
                bandera = False
