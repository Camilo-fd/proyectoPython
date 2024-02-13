from programa.camper import camper
from os import system
from .valido import menuNoValid
from .datos import notas,camper,notasModulo
from programa.camper import listarCamper
from programa.modulo import listar
from programa.trainer import listarTrainer
import json

def pruebaSeleccion(): 
    info = {
        "Nro Identificacion": input("Nro Identificacion Camper: "),
        "Fecha": input("Fecha: "),
        "Nota": notaSeleccion()
    }
    # notas.append(info)
    # with open("programa/datosJson/notas.json", "w") as f:
    #     data = json.dumps(notas, indent=4)
    #     f.write(data)
    #     f.close()
    #     system("clear")
    return info

def notaSeleccion():
    notaPractica = int(input("Nota Practica: "))
    notaTeorica = int(input("Nota Teorica: "))
    promedio = int((notaPractica+notaTeorica) / 2)
    return promedio

def asignarPrueba(): #Inicial
    print("""\033[92m
        **************************
        * Asignar Prueba Inicial *
        **************************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
            camper = json.loads(f.read())
            f.close()
            listarCamper()
    codigoCamper = input("Nro Identificacion del camper: ")
    with open("programa/datosJson/notas.json", "r") as f:
        nota = json.loads(f.read())
        f.close()
    print("                                   ")
    print("-----------------------------------")
    info = pruebaSeleccion()
    nota.append(info)
    with open("programa/datosJson/notas.json","w") as f:
        data = json.dumps(nota, indent=4)
        f.write(data)
        f.close()
        system("clear")
    for item in nota:
        print("\t    --------------NOTA-------------")
        for key, value in item.items():
            print(f"\t    {key}: {value}")
        print("\t    -------------------------------")
    for campers in camper:
            if campers.get("Nro Identificacion") == codigoCamper:
                for notas in nota:
                    if notas.get("Nro Identificacion") == codigoCamper:
                        campers["Nota"].append(notas)
                        if notas.get("Nota") >= 60:
                            campers["Estado"] = "Inscrito"
    with open("programa/datosJson/camper.json", "w") as f:
        campers = json.dumps(camper, indent=4)
        f.write(campers)
        f.close()

def notaModulo():
    
    info = {
        "Nro Identificacion": input("Nro Identificacion Camper: "),
        "modul": listar(),
        "Codigo": input("Codigo Modulo: "),
        "Total": calculosnotaModulo(),
        "Fecha": input("Fecha: "),
        "Nro Identificaion Trainer": input("Nro Identificacion Trainer: ")
    }
    return info

def calculosnotaModulo():
    notaProyecto = int(input("Nota Proyecto: "))
    notaExamen = int(input("Nota Examen: "))
    notaGenerales = int(input("Nota Generales: "))
    proPruebas = (notaProyecto * 0.3) + (notaExamen * 0.6)
    promedio = int(proPruebas + (notaGenerales * 0.1))
    return promedio

def asignarNotamodulo():
    print("""\033[92m
        ***********************
        * Asignar Nota Modulo *
        ***********************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        f.close()
        listarCamper()
    codigoCamper = input("Nro Identificacion del camper: ")
    with open("programa/datosJson/notasModulo.json", "r") as f:
        notasModulo = json.loads(f.read())
        f.close()
    print("                                   ")
    print("-----------------------------------")
    info = notaModulo()
    for item in notasModulo:
        print("\t    ----------NOTA MODULO----------")
        for key, value in item.items():
            print(f"\t    {key}: {value}")
        print("\t    -------------------------------")
    for campers in camper:
            if campers.get("Nro Identificacion") == codigoCamper:
                campers["Nota Modulo"].append(info)
                for notas in notasModulo:
                    if notas.get("Nro Identificacion") == codigoCamper:
                        campers["Nota Modulo"].append(notasModulo)
                        if notas["Total"] >= 60:
                            campers["Estado"] = "Aprovado"
                        else:
                            campers["Estado"] = "En Riesgo"
    with open("programa/datosJson/camper.json", "w") as f:
        campers = json.dumps(camper, indent=4)
        f.write(campers)
        f.close()
    with open("programa/datosJson/notasModulo.json", "w") as f:
        nota = json.dumps(notasModulo, indent=4)
        f.write(nota)
        f.close()

def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -             MENU NOTAS                -
    -----------------------------------------
    -     1. Asignar Prueba Seleccion       -
    -     2. Asignar Nota Modulo            -
    -     3. Eliminar                       -
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
                asignarPrueba()
            case 2:
                system("clear")
                asignarNotamodulo()
            case 3:
                system("clear")
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)()