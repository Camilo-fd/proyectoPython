import json
from os import system
from programa.valido import menuNoValid
import programa.camper as camper 
import programa.trainer as trainer
import programa.notas as notas
import programa.ruta as ruta
import programa.modulo as modulo
import programa.horario as horario
import programa.salasEntrenamiento as salasEntrenamiento
import programa.reportes as reportes

def menu():
    print("""
    -----------------------------------------
    -         MENU ADMINISTRACION           -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Camper                         -
    -     2. Trainer                        -
    -     3. Notas                          -
    -     4. Rutas                          -
    -     5. Modulos                        -
    -     6. Horarios                       -
    -     7. Salas Entrenamiento            -
    -     8. Reportes                       -
    -     0. Salir                          -
    -----------------------------------------
""")
bandera = True
while (bandera):
    menu()
    try:
        opc = int(input())
    except ValueError:
        system("clear")
        continue
    match(opc):
        case 1:
            with open("programa/datosJson/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                camper.menu()
            system("clear")
        case 2:
            with open("programa/datosJson/trainer.json", "r") as f:
                trainer.trainer = json.loads(f.read())
                f.close()
                system("clear")
                trainer.menu()
            system("clear")
        case 3:
            with open("programa/datosJson/notas.json", "r") as f:
                notas.notas = json.loads(f.read())
                f.close()
                system("clear")
                notas.menu()
            system("clear")
        case 4:
            with open("programa/datosJson/ruta.json", "r") as f:
                ruta.ruta = json.loads(f.read())
                f.close()
                system("clear")
                ruta.menu()
            system("clear")
        case 5:
            with open("programa/datosJson/modulo.json", "r") as f:
                modulo.modulo = json.loads(f.read())
                f.close()
                system("clear")
                modulo.menu()
            system("clear")
        case 6:
            with open("programa/datosJson/horario.json", "r") as f:
                horario.horario = json.loads(f.read())
                f.close()
                system("clear")
                horario.menu()
            system("clear")
        case 7:
            with open("programa/datosJson/salasEntrenamiento.json", "r") as f:
                salasEntrenamiento.salasEntrenamiento = json.loads(f.read())
                f.close()
                system("clear")
                salasEntrenamiento.menu()
            system("clear")
        case 8:
                system("clear")
                reportes.menu()
                system("clear")
        case 0:
            bandera = False
        case _:
            menuNoValid(opc)