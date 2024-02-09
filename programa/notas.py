# from programa.camper import camper
from os import system
from .valido import menuNoValid
from .datos import notas
import json

def pruebaSeleccion():  
    info = {
        "Nro Identificacion": int(input("Nro Identificacion Camper: ")),
        "Fecha": input("Fecha: "),
        "Nota": notaSeleccion(),
        "Estado": "Inscrito"
    }
    notas.append(info)
    with open("programa/datosJson/notas.json", "w") as f:
        data = json.dumps(notas, indent=4)
        f.write(data)
        f.close()
        system("clear")

def notaSeleccion():
    notaPractica = int(input("Nota Practica: "))
    notaTeorica = int(input("Nota Teorica: "))
    promedio = int((notaPractica+notaTeorica) / 2)
    return promedio

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

# def notasCamper():
#     info = {
#         "Nro Identificacion": int(input("Nro Identificacion Camper: ")),
#         "Codigo": input("Codigo Modulo: "),
#         "Notas Proyecto": int(input("Nota Proyecto: ")),
#         "Notas Generales": [],
#         "Total": 
#     }

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
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
        match(opc):
            case 1:
                system("clear")
                pruebaSeleccion()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)