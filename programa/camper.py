import json
from os import system
from .datos import camper
from .valido import menuNoValid

def guardar():
    info = {
        "Nro Identificacion": int(input("Ingrese su numero de identificacion: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido: "),
        "Direccion": input("Ingrese la direccion: "),
        "Telefonos": [],
        "Acudiente": input("Ingrese su acudiente: "),
        "Estado": "Pre inscrito"
    }
    camper.append(info)
    with open("programa/datosJson/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Camper"

def editar():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        * Acualizacion Camper *
        ***********************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {camper[codigo].get('Nombre')}
    Apellido: {camper[codigo].get('Apellido')}
    Edad: {camper[codigo].get('Edad')}
    Genero: {camper[codigo].get('Genero')}
    ________________________
        """)
        print("¿Este es el camper que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del camper\n"),
                "Apellido": input("Ingrese el apellido del camper\n"),
                "Edad": int(input("Ingrese la edad del camper\n")),
            }
            camper[codigo] = info
            with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")
    return "Edit to camper"

def buscar():
    system("clear")
    print(f"""
    *******************
    *  Lista Campers  *
    *******************
    """)
    for i,val in enumerate(camper):
        print(f"""
    ____________________________
    Codigo: {i}
    Nombre: {val.get('Nombre')}
    Apellido: {val.get('Apellido')}
    Edad: {val.get('Edad')}
    Genero: {val.get('Genero')}
    ____________________________
        """)
    return "The camper is avaliable"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Ingresar Camper")
        print("\t2. Editar Camper")
        print("\t3. Buscar Camper")
        print("\t4. Eliminar Camper")
        print("\t0. Salir")
        opc = int(input())
        match(opc):
            case 1:
                system("clear")
                guardar()
            case 1:
                system("clear")
                editar()
            case 1:
                system("clear")
                buscar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)