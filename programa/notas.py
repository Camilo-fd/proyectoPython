from programa.camper import camper
from os import system
from .valido import menuNoValid
from .datos import notas,camper
import json

def pruebaSeleccion():  
    info = {
        "Nro Identificacion": input("Nro Identificacion Camper: "),
        "Fecha": input("Fecha: "),
        "Nota": notaSeleccion()
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

def asignarPrueba():
        with open("programa/datosJson/camper.json", "r") as f:
                camper = json.loads(f.read())
                f.close()
                for item in camper:
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print("")
        codigoCamper = input("Nro Identificacion del camper: ")
        with open("programa/datosJson/notas.json", "r") as f:
            nota = json.loads(f.read())
            f.close()
            for item in nota:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("")
        for campers in camper:
            if campers.get("Nro Identificacion") == codigoCamper:
                for notas in nota:
                    if notas.get("Nro Identificacion") == codigoCamper:
                        campers["Nota"].append(notas)
                        if notas.get("Nota") >= 60:
                            campers["Estado"] = "Aprobado"
        with open("programa/datosJson/camper.json", "w") as f:
            campers = json.dumps(camper, indent=4)
            f.write(campers)
            f.close()

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
            case 2:
                system("clear")
                asignarPrueba()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)