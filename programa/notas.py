from programa.camper import buscar
from os import system
from .valido import menuNoValid

def ingresar():
    print("")

def editar():
    print("")

def buscar():
    print("")

def eliminar():
    print("")

def menu():
    bandera = True
    while (bandera):
        print(f"""
    *****************
    *  Menu Notas  *
    *****************
    """)
        print("\t1. Ingresar Notas")
        print("\t2. Editar Notas")
        print("\t3. Buscar Notas Camper")
        print("\t4. Eliminar Notas")
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
            case 3:
                system("clear")
                buscar()
            case 4:
                system("clear")
                eliminar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)