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
        print("Modulo registrado correctamente")

def editar():
    bandera = True
    while (bandera):
        codigo = int(input("Ingrese el codigo del modulo: "))
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
                bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")


def menu():
    bandera = True
    while (bandera):
        print("\t1. Crear Modulo")
        print("\t2. Editar Modulo")
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