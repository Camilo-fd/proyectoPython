import json
from os import system
from .datos import camper
from .valido import menuNoValid

def guardar():
    info = {
        "Nro Identificacion": int(input("Ingrese su numero de identificacion: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Direccion": input("Ingrese la direccion del camper: "),
        "Telefonos": [
            {
            f"{'Fijo' if(int(input('\t.1 fijo\t2. Celular: '))) else 'Celular'}":
            int(input(f'Numero de contactto {x+1}: '))
        }

        for x in range(int(input("Ingrese la cantidad de telefonos que tiene: ")))

        ],
        "Acudiente": input("Ingrese su acudiente: "),
        "Estado": "Pre inscrito"
    }
    camper.append(info)
    with open("programa/datosJson/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
        system("clear")
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
        codigo = int(input("Ingrese el codigo del camper: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nro Identificacion: {camper[codigo].get('Nro Identificacion')}
    Nombre: {camper[codigo].get('Nombre')}
    Apellido: {camper[codigo].get('Apellido')}
    Direccion: {camper[codigo].get('Direccion')}
    Telefonos: {camper[codigo].get('Telefonos')}
    ________________________
        """)
        print("¿Este es el camper que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
        "Nro Identificacion": int(input("Ingrese su numero de identificacion: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Direccion": input("Ingrese la direccion del camper: "),
        "Telefonos": [
            {
                #Hay error al concatenar el x+1, !SOLUCIONARLO!
                f"{'Fijo' if(int(input('1. fijo 2. Celular: '))) else 'Celular'}":
                int(input(f'Numero de contacto {x+1}: '))
            }

            for x in range(int(input("Ingrese la cantidad de telefonos: ")))
        ],
        "Acudiente": input("Ingrese su acudiente: "),
        "Estado": "Pre inscrito"
    }
            camper[codigo] = info
            with open("programa/datosJson/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
            system("clear")

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
    Nro Identificacion: {val.get('Nro Identificacion')}
    Nombre: {val.get('Nombre')}
    Apellido: {val.get('Apellido')}
    Direccion: {val.get('Direccion')}
    Telefonos: {val.get('Telefonos')}
    ____________________________
        """)
    return "The camper is avaliable"

def borrar():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion Camper  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nro Identificacion: {camper[codigo].get('Nro Identificacion')}
    Nombre: {camper[codigo].get('Nombre')}
    Apellido: {camper[codigo].get('Apellido')}
    Direccion: {camper[codigo].get('Direccion')}
    Telefonos: {camper[codigo].get('Telefonos')}
    ________________________
        """)
        print("¿Este es el camper que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo)
            with open("programa/datosJson/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 2):
            print("________________________")
            print("Que desea hacer entonces?")
            print("1. Volver al menu")
            print("2. Eliminar camper")
            opc2 = int(input())
            if (opc2 == 1):
                system("clear")
                menu()
            elif (opc2 == 2):
                system("clear")
                camper.pop(codigo)
                with open("programa/datosJson/camper.json", "w") as f:
                    data = json.dumps(camper, indent=4)
                    f.write(data)
                    f.close()
        elif(opc == 3):
            bandera = False
    return "Camper deleted"

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
            case 2:
                system("clear")
                editar()
            case 3:
                system("clear")
                buscar()
            case 4:
                system("clear")
                borrar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)