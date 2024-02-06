import json
from os import system
from .datos import ruta
from programa.modulo import modulo

def ingresar():
    info = {
        "Nombre Ruta": input("Nombre de la ruta: "),
        "Codigo": int(input("Codigo: ")),
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
    Nombre Ruta: {ruta[codigo].get('Nombre Ruta')}
    Modulo: {ruta[codigo].get('Modulo')}
    Codigo: {codigo}
        """)

# def cargar():
#     with open("programa/datosJson/ruta.json", "r") as f:
#         return json.loads(f.read())


# def plantilla(data):
#     lista = []
#     for i,val in enumerate(data):
#         lista.append(f"\n\t\t{i+1} - {val}")
#     return "".join(lista)


# def asignarModulos():
#     # Temario: {"".join([f"{i} - {val}" for i,val in enumerate(val.get("temario"))])}
#     selecion = set()
#     nuevaLista = []
#     while(True):
#         for val in modulo:
#             print(f"""
#             ________________
#             Codigo: {val.get("codigo")}
#             Nombre: {val.get("nombre_modulo")}
#             Prioridad: {val.get("prioridad")}
#             Temario: {plantilla(val.get("temario"))}
#             ________________
#             """)

#         selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
#         if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
#             for i in selecion:
#                 for val in modulo:
#                    if(val.get("codigo") == i):
#                         nuevaLista.append(val)
#             break
#     return nuevaLista


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
        print("\r3. Asiganar ruta")
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