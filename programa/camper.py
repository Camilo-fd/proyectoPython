import json
from os import system
from .datos import camper
from .valido import menuNoValid

def guardar():
    print(f"""
    *********************
    *  Ingresar Camper  *
    *********************
    """)

    info = {
        "Nro Identificacion": int(input("Ingrese su numero de identificacion: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Direccion": input("Ingrese la direccion del camper: "),
        "Telefonos": [
            {
            f"{'Fijo' if(int(input('1. Fijo 2. Celular: '))) else 'Celular'}":
            int(input(f'Numero de contactto {x+1}: '))
        }

        for x in range(int(input("Ingrese la cantidad de telefonos que tiene: ")))

        ],
        # "Acudiente": input("Ingrese su acudiente: "),
        "Acudiente": [],
        "Estado": "Pre inscrito"
    }

    edad = int(input("Ingrese la edad del camper: "))
    if edad < 16:
        system("clear")
        return print('''
                     No tienes la edad suficiente
                     ''')
    elif edad > 28:
        system("clear")
        return print('''
                     Excedes el limite de edad
                     ''')
    elif edad >=18:
        exit
    elif 16 <= edad < 18:
        info["Responsable"] = input("Ingrese su acudiente: ")
        info["Acudiente"].append({"Responsable": info["Responsable"] })

    camper.append(info)
    with open("programa/datosJson/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
        system("clear")
    print("                               ")
    print("Camper registrado correctamente")
    print("                               ")

def editar():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        *****************
        * Editar Camper *
        *****************
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
    Verificacion: {camper[codigo].get('Verificacion')}
    Estado: {camper[codigo].get('Estado')}
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
                f"{'Fijo' if(int(input('1. Fijo 2. Celular: '))) else 'Celular'}":
                int(input(f'Numero de contacto {x+1}: '))
            }

            for x in range(int(input("Ingrese la cantidad de telefonos: ")))
        ],
        "Acudiente": [],
        "Estado": input("")
    }
        edad = int(input("Ingrese la edad del camper: "))
        if edad < 16:
            print("No tienes la edad suficiente")
            exit
        elif edad >=18:
            exit
        elif 16 <= edad < 18:
            info["Responsable"] = input("Ingrese su acudiente: ")
            info["Acudiente"].append({
                # "Edad": edad,
                "Responsable": info["Responsable"]
            })
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
    numr = 0
    numr = int(input("Escribe tu numero de registro: "))
    print(f"""
    *******************
    *  Buscar Camper  *
    *******************
    """)

    for i, val in enumerate(camper):
        telefonos = ""
        for valor in val.get('Telefonos'):
            for key, value in valor.items():
                telefonos += f" {key} = {value} "

    for i,val in enumerate(camper):
        if (val.get('Nro Identificacion') == numr):
            print(f"""
    ____________________________
    Codigo: {i}
    Nro Identificacion: {val.get('Nro Identificacion')}
    Nombre: {val.get('Nombre')}
    Apellido: {val.get('Apellido')}
    Direccion: {val.get('Direccion')}
    Telefonos: {telefonos}
    Verificacion: {val.get('Verificacion')}
    Estado: {val.get('Estado')}
    ____________________________
        """)
    return "The camper is avaliable"

def borrar():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ********************
        * Eliminar Camper  *
        ********************
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
    Verificacion: {camper[codigo].get('Verificacion')}
    Estado: {camper[codigo].get('Estado')}
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
        print(f"""
    *****************
    *  Menu Camper  *
    *****************
    """)
        print("\t1. Ingresar Camper")
        print("\t2. Editar Camper")
        print("\t3. Buscar Camper")
        print("\t4. Eliminar Camper")
        print("\t0. Salir")
        try:
            opc = int(input())
        except ValueError:
            system("clear")
            continue
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