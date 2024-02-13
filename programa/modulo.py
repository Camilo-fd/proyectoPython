import json
from .datos import modulo
from os import system

def crear():
    print(f"""\033[92m
    *********************
    *    Crear Modulo   *
    *********************
    \033[92m""")
    while True:
        codigo = input("Codigo Modulo: ")
        for modulos in modulo:
                if modulos["Codigo"] == codigo:
                    print("                                                           ")
                    print("Este Codigo de modulo ya esta creado, ingrese uno diferente")
                    break
        else:
                   break
    info = {
        "Codigo": codigo,
        "Nombre Modulo": input("Nombre Modulo: "),
        "Prioridad": input("Prioridad: "),
        "Temarios": []
        
    }
    for x in range(int(input("Numero de temarios: "))):
        info["Temarios"].append({"Temario":input("Nombre temario:")})

    modulo.append(info)
    with open("programa/datosJson/modulo.json", "w") as f:
        datos = json.dumps(modulo, indent=4)
        f.write(datos)
        f.close()
        system("clear")
        print("Modulo registrado correctamente")

def editar():
    print(f"""\033[92m
    *********************
    *   Editar Modulo   *
    *********************
    \033[92m""")
    bandera = True
    while (bandera):
        codigo = input("Ingrese el codigo del modulo: ")
        print(f"""
        Codigo: {codigo}
        Nombre Modulo: {modulo[codigo].get('Nombre Modulo')}
        Prioridad: {modulo[codigo].get('Prioridad')}
        Temarios: {modulo[codigo].get('Temarios')}
            """)
        print("¿Este es el modulo que deseas modificar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        if (opc == 1):
                info = {
        "Codigo": input("Codigo: "),
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
                bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")

def listar():
    system("clear")
    print(f"""\033[92m
    **********************
    *    Listar Modulo   *
    **********************
    \033[92m""")
    with open("programa/datosJson/modulo.json") as f:
        modulos = json.loads(f.read())
        f.close()
    for modulo in modulos:
         printModulo(modulo)

def printModulo(modulo): # IMPRIMO EL MODULO LINDO
    print(f"""\033[92m
            ----------------MODULO-------------
            Codigo: {modulo["Codigo"]}
            Nombre Modulo: {modulo["Nombre Modulo"]}
            Prioridad: {modulo["Prioridad"]}
            Temarios: {listadomodulo(modulo)}
            -----------------------------------
              \033[92m""")
    
def listadomodulo(modulo): # LISTO LOS TEMARIOS DEL MODULO
    texto=""
    for i in modulo["Temarios"]:
        texto+=f'\n\t\t     {i["Temario"]} '
    return (texto)

def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -            MENU MODULOS               -
    -----------------------------------------
    -     1. Crear Modulo                   -
    -     2. Editar Modulo                  -
    -     3. Buscar Modulo                  -
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
                crear()
            case 2:
                system("clear")
                editar()
            case 3:
                system("clear")
                listar()
            case 0:
                system("clear")
                bandera = False