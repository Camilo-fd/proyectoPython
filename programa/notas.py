# from programa.camper import camper
from os import system
from .valido import menuNoValid
# from .datos import camper
import json

def pruebaSeleccion():
    info = {
        "Nro Identificacion": int(input("Nro Identificacion Camper: ")),
        "Fecha": input("Fecha: "),
        "Nota": int(input("Nota: "))
    }
    
# def asignarPrueba():
#         with open("programa/datosJson/camper.json", "r") as f:
#                 camper = json.loads(f.read())
#                 f.close()
#         codigoCamper = int(input("Codigo del camper: "))
#         print(f"{camper[codigoCamper]}")
#         with open("programa/datosJson/notas.json", "r") as f:
#             nota = json.loads(f.read())
#             f.close()
#         while True:
#             pruebaInicial.append(campers[codigoCamper])
#             with open("programa/datosJson/ruta.json", "w") as f:
#                 campers = json.dumps(campers, indent=4)
#                 f.write(campers)
#                 f.close()
#                 break

def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -             MENU NOTAS                -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Ingresar Notas                 -
    -     4. Eliminar Notas                 -
    -     0. Salir                          -
    -----------------------------------------
""")
        print("\t1. Ingresar Notas")
        print("\t4. Eliminar Notas")
        print("\t0. Salir")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            # case 1:
            #     system("clear")
            #     asignarPrueba()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)