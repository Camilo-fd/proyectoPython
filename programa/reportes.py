import json
from os import system
from .valido import menuNoValid
from programa.trainer import listarTrainer
from programa.ruta import listarRuta

def camperInscrito():
    print("""\033[92m\t\t
        *******************
        * Campers Inscritos *
        *******************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Inscrito":
                print("\033[92m\t\t--------------------------------------\033[92m")
                print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                print(f"\t\tNombre: {campers['Nombre']}")
                print(f"\t\tApellido: {campers['Apellido']}")
                print(f"\t\tDireccion: {campers['Direccion']}")
                print(f"\t\tCelular: {campers['Celular']}")
                print(f"\t\tFijo: {campers['Fijo']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print("\t\t--------------------------------------")
                print("                                      ")

def recorrerNota():
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for campers in camper["Nota"]:
            print(campers.get("Nro Identificacion"))

def camperAprobado():
    print("""\033[92m\t\t
        *******************
        * Campers Aprobado *
        *******************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Aprobado":
                print("\033[92m\t\t--------------------------------------\033[92m")
                print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                print(f"\t\tNombre: {campers['Nombre']}")
                print(f"\t\tApellido: {campers['Apellido']}")
                print(f"\t\tCelular: {campers['Celular']}")
                print(f"\t\Fijo: {campers['Fijo']}")
                print(f"\t\tDireccion: {campers['Direccion']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print("\t\t--------------------------------------")
                print("                                      ")

def camperBajoriesgo():
    print("""\033[92m\t\t
        ***********************
        * Campers Bajo Riesgo *
        ***********************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "En Riesgo":
                print("\033[92m\t\t--------------------------------------\033[92m")
                print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                print(f"\t\tNombre: {campers['Nombre']}")
                print(f"\t\tApellido: {campers['Apellido']}")
                print(f"\t\tDireccion: {campers['Direccion']}")
                print(f"\t\tCelular: {campers['Celular']}")
                print(f"\t\Fijo: {campers['Fijo']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print("\t\t--------------------------------------")
                print("                                   ")
                # print(json.dumps(campers, indent=4))

def mostraTrainer():
    listarTrainer()

def listarCamperTrainerRuta():
    print("""\033[92m\t\t
        ********************************
        * Camper Trainer Asigando Ruta *
        ********************************
        \033[92m""")
    with open("programa/datosJson/ruta.json", "r") as f:
        ruta = json.loads(f.read())
    listarRuta()
    codRuta = input("Codigo Ruta: ")
    system("clear")
    for rutas in ruta:
        if rutas.get("Codigo") == codRuta:
                for campers in rutas["Camper"]:
                    print("\t\t-----------------CAMPER----------------------")
                    print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                    print(f"\t\tNombre: {campers['Nombre']}")
                    print(f"\t\tApellido: {campers['Apellido']}")
                    print(f"\t\tDireccion: {campers['Direccion']}")
                    print(f"\t\tCelular: {campers['Celular']}")
                    print(f"\t\Fijo: {campers['Fijo']}")
                    print(f"\t\tAcudiente: {campers['Acudiente']}")
                    print(f"\t\tEstado: {campers['Estado']}")
                    print("\t\t--------------------------------------")
                    print("                                      ")
                for trainers in rutas["Trainer"]:
                        try:
                            trai = trainers['Nombre Completo']
                        except KeyError:
                            trai = ""
                        print("\t\t-----------------TRAINER---------------------")
                        print(f"\t\tNro Identificacion: {trainers['Nro Identificacion']}")
                        print(f"\t\tNombre Completo: {trai}")
                        print("\t\t--------------------------------------")
                        print("                                      ")

def CamperTrainerRuta():
    with open("programa/datosJson/ruta.json","r") as f:
        ruta = json.loads(f.read())
        system("clear")
    for rutas in ruta:
        print("                            ")
        print("\t----Ruta----")
        print(f"\t Codigo: {rutas.get('Codigo')}")
        print(f"\t Nombre Ruta: {rutas.get('Nombre Ruta')}")
        # print(f"\t Camper: {rutas.get('Camper')}")
        # print(f"\t Trainer: {rutas.get('Trainer')}")
        for trainers in rutas["Trainer"]:
            print("                            ")
            print("\t----Trainer----")
            for key, value in trainers.items():
                if key != "Camper":
                    print(f"\t{str(key)}  :  {str(value)}")
        for campers in rutas["Camper"]:
            for i in campers["Nota Modulo"][0]:
                if float(i ["Total"]) > 60:
                    print("                            ")
                    print(f"\t----Camper Paso-----\n\tNro Identificacion: {campers['Nro Identificacion']}\n\tNombre: {campers['Nombre']}\n\tApellido: {campers['Apellido']}")
                else:
                        print("                            ")
                        print(f"\t----Camper no paso:----- \n\tNro Identificacion: {campers['Nro Identificacion']}\n\tNombre: {campers['Nombre']}\n\tApellido: {campers['Apellido']}")


def menu():
    bandera = True
    while (bandera):
        print("""\033[94m
    -----------------------------------------
    -             MENU Reportes             -
    -----------------------------------------
    -     1. Listar Camper Inscritos        -
    -     2. Listar Camper Aprovados        -
    -     3. Listar Trainer                 -
    -     4. Listar Camper En Riesgo        -
    -     5. Listar Camper y Trainer        -
    -          asociados a una ruta         -
    -     6. Listar Camper Perdieron        -
    -           Y Aprovaron Dependiendo     -
    -           De Ruta                     -
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
                camperInscrito()
            case 2:
                system("clear")
                camperAprobado()
            case 3:
                system("clear")
                mostraTrainer()
            case 4:
                system("clear")
                camperBajoriesgo()
            case 5:
                system("clear")
                listarCamperTrainerRuta()
            case 6:
                system("clear")
                CamperTrainerRuta()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)