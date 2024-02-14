from .datos import horario
import json
from os import system
from programa.valido import menuNoValid

def guardarhorarios():
    print(f"""\033[92m
    *********************
    *  Guardar Horario  *
    *********************
    \033[92m""")
    info = {
    "Nombre Jornada": input("Nombre Jornada: "),
    "Codigo": input("Codigo: "),
    "Hora": input("Hora: ")
}
    horario.append(info)
    with open("programa/datosJson/horario.json", "w") as f:
        data = json.dumps(horario, indent=4)
        f.write(data)
        f.close()

def prinHorario():
    with open("programa/datosJson/horario.json") as f:
        horario = json.loads(f.read())
    for horarios in horario:
    # try:
    #     nota = camper["Nota"][0]["Nota"]
    # except IndexError:
    #     nota = ""
    # try:
    #     notaModulo = camper["Nota Modulo"][0]["Total"]
    # except IndexError:
    #     notaModulo = ""
        print(f"""\033[92m
            ----------------CAMPER-------------
            Nombre Jornada: {horarios["Nombre Jornada"]}
            Codigo: {horarios["Codigo"]}
            Hora: {horarios["Hora"]}
            -----------------------------------
              \033[92m""")

def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -            MENU HORARIO               -
    -----------------------------------------
    -   Sistema de almacenamiento de datos  -
    -     1. Guardar horario                -
    -     2. Buscar horario                 -
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
                guardarhorarios()
            case 2:
                prinHorario()
            case 0:
                bandera = False
            case _:
                menuNoValid(opc)