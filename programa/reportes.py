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
                print(f"\t\tTelefonos: {campers['Telefonos']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print(f"\t\tNota: {campers['Nota']}")
                print(f"\t\tNota Modulo: {campers['Nota Modulo']}")
                print("\t\t--------------------------------------")
                print("                                      ")
                # print(json.dumps(campers, indent=4))

def camperAprovado():
    print("""\033[92m\t\t
        *******************
        * Campers Aprovado *
        *******************
        \033[92m""")
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        for i,campers in enumerate(camper):
            if camper[i]["Estado"] == "Aprovado":
                print("\033[92m\t\t--------------------------------------\033[92m")
                print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                print(f"\t\tNombre: {campers['Nombre']}")
                print(f"\t\tApellido: {campers['Apellido']}")
                print(f"\t\tDireccion: {campers['Direccion']}")
                print(f"\t\tTelefonos: {campers['Telefonos']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print(f"\t\tNota: {campers['Nota']}")
                print(f"\t\tNota Modulo: {campers['Nota Modulo']}")
                print("\t\t--------------------------------------")
                print("                                      ")
                # print(json.dumps(campers, indent=4))

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
                print(f"\t\tTelefonos: {campers['Telefonos']}")
                print(f"\t\tAcudiente: {campers['Acudiente']}")
                print(f"\t\tEstado: {campers['Estado']}")
                print(f"\t\tNota: {campers['Nota']}")
                print(f"\t\tNota Modulo: {campers['Nota Modulo']}")
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
    for rutas in ruta:
        if rutas.get("Codigo") == codRuta:
                for campers in rutas["Camper"]:
                    print("\t\t--------------------------------------")
                    print(f"\t\tNro Identificacion: {campers['Nro Identificacion']}")
                    print(f"\t\tNombre: {campers['Nombre']}")
                    print(f"\t\tApellido: {campers['Apellido']}")
                    print(f"\t\tDireccion: {campers['Direccion']}")
                    print(f"\t\tTelefonos: {campers['Telefonos']}")
                    print(f"\t\tAcudiente: {campers['Acudiente']}")
                    print(f"\t\tEstado: {campers['Estado']}")
                    print(f"\t\tNota: {campers['Nota']}")
                    print(f"\t\tNota Modulo: {campers['Nota Modulo']}")
                    print("\t\t--------------------------------------")
                    print("                                      ")
                    # print(json.dumps(campers, indent=4))
                for trainers in rutas["Trainer"]:
                    print("\t\t--------------------------------------")
                    print(f"\t\tNro Identificacion: {trainers['Nro Identificacion']}")
                    print(f"\t\tNombre Completo: {trainers['Nombre Completo']}")
                    print("\t\t--------------------------------------")
                    print("                                      ")
                    # print(json.dumps(trainers, indent=4))
        # elif rutas.get("Codigo") != codRuta:
        #     system("clear")
        #     print("No hay Camper y Trainer en una ruta")
        #     exit

def CamperTrainerRuta():
    with open("programa/datosJson/ruta.json","r") as f:
        ruta = json.loads(f.read())
        system("clear")
    for rutas in ruta:
        print("                            ")
        print("\t----Ruta----")
        for key, value in rutas.items():
            print(f"{key}  :  {str(value)}")
        for trainers in rutas["Trainer"]:
            print("                            ")
            print("\t----Trainer----")
            for key, value in trainers.items():
                print(f"{str(key)}  :  {str(value)}")
        for campers in rutas["Camper"]:
            for i in campers["Nota Modulo"][0]:
                if float(i ["Total"]) > 60:
                    print("                            ")
                    print(f"\t----Camper Paso-----\n{campers}")
                elif float(i ["Total"]) < 60:
                    print("                            ")
                    print(f"\t----Camper no paso:----- \n{campers}")

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
                camperAprovado()
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