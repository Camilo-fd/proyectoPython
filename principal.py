import json
from os import system
import programa.camper as camper 
import programa.trainer as trainer
from programa.valido import menuNoValid
import programa.notas as notas

def menu():
    print("""
        ************************
        * Menu Adiministracion *
        ************************
        """)
    print("Sistema de almacenamiento de dato")
    print("\t1. Camper")
    print("\t2. Trainer")
    print("\t3. Notas")
    print("\t0. Salir")
bandera = True
while (bandera):
    menu()
    opc = int(input())
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
            with open("programa/datosJson/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                notas.note()
        case 0:
            bandera = False
        case _:
            menuNoValid(opc)