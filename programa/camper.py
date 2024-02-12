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
    while True:
        NroIdentifiacion = input("Ingrese su numero de identificacion: ")
        if NroIdentifiacion.isdigit():
            break
        else:
            print("Ingrese solo numero")

    info = {
        "Nro Identificacion": NroIdentifiacion,
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Direccion": input("Ingrese la direccion del camper: "),
        "Telefonos": [
            {
            f"{'Fijo' if(int(input('1. Fijo 2. Celular: '))==1) else 'Celular'}":
            int(input(f'Numero de contactto {x+1}: '))
        }

        for x in range(int(input("Ingrese la cantidad de telefonos que tiene: ")))

        ],
        "Acudiente": [],
        "Estado": "Pre inscrito",
        "Nota": [],
        "Nota Modulo": []
    }
    bandera = True
    while (bandera):
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
            bandera  = False
        elif 16 <= edad < 18:
            info["Acudiente"].append({"Responsable": input("Ingrese el nombre del acudiente: ")})
        camper.append(info)
        with open("programa/datosJson/camper.json", "w") as f:
            data = json.dumps(camper, indent=4)
            f.write(data)
            f.close()
        bandera = False
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
        listarCamper()
        codigo = input("Ingrese el Nro Identificacion del camper que deseas actualizar: ")
        try:
            codCamper = next(index for index, camp in enumerate(camper) if camp.get("Nro Identificacion") == codigo)
            print(f"""
    ________________________
    Nro Identificacion: {camper[codCamper].get('Nro Identificacion')}
    Nombre: {camper[codCamper].get('Nombre')}
    Apellido: {camper[codCamper].get('Apellido')}
    Direccion: {camper[codCamper].get('Direccion')}
    Telefonos: {camper[codCamper].get('Telefonos')}
    Acudiente: {camper[codCamper].get('Acudiente')}
    Estado: {camper[codCamper].get('Estado')}
    ________________________
        """)
            print("¿Esta seguro de actualizar este camper?")
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
            # "Acudiente": [info["Acudiente"].append({"Responsable": input("Ingrese el nombre del acudiente: ")})],
            "Estado": "Pre Inscrito"
        }
                # info["Acudiente"].append({"Responsable": input("Ingrese el nombre del acudiente: ")})
                camper[codCamper] = info
                with open("programa/datosJson/camper.json", "w") as f:
                        data = json.dumps(camper, indent=4)
                        f.write(data)
                        f.close()
                bandera = False
                system("clear")
            elif (opc == 2):
                bandera = False
                editar
            elif(opc == 3):
                bandera = False
                system("clear")
        except StopIteration:
                print("ERROR. no se encuentra ese codigo")
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
        
    with open("programa/datosJson/camper.json", "r") as f:
        camper = json.loads(f.read())
        f.close()

    for i, val in enumerate(camper):
        telefonos = ""
        for valor in val.get('Telefonos'):
            for key, value in valor.items():
                telefonos += f" {key} = {value} "

    for i,val in enumerate(camper):
        if (val.get('Nro Identificacion') == numr):
            print(f"""
    ____________________________
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

def listarCamper():
    system("clear")
    with open("programa/datosJson/camper.json") as f:
        campers = json.loads(f.read())
        f.close()
    for camper in campers:
         printCamper(camper)

def printCamper(camper):
    print(f"""
            ----------------CAMPER-------------
            Nro Identificacion: {camper["Nro Identificacion"]}
            Nombre: {camper["Nombre"]}
            Apellido: {camper["Apellido"]}
            Direccion: {camper["Direccion"]}
            Telefonos: {"".join([f"{list(camper['Telefonos'][ind].keys())[0]}: {list(camper['Telefonos'][ind].values())[0]}" for ind,val in enumerate(camper["Telefonos"])])}
            Acudiente: {camper["Acudiente"]}
            Estado: {camper["Estado"]}
            Nota: {camper["Nota"]}
            Nota Modulo: {camper["Nota Modulo"]}
            -----------------------------------
              """) 


def listadoacudiente(camper):
            for i in camper["Acudiente"]:
                return(f"""
                    Responsable: {i["Responsable"]}
                      """)

def listadotelefonos(camper):
    for i in camper["Telefonos"]:
        return(f"""
                Telefonos: {i["Responsable"]}
                  """)
    
def borrar():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ********************
        * Eliminar Camper  *
        ********************
        """)
        listarCamper()
        codigo = input("Ingrese el codigo del camper que deseas eliminar \n")
        try:
            codCamper = next(index for index, camp in enumerate(camper) if camp.get("Nro Identificacion") == codigo)
            print(f"""
    ________________________
    Nro Identificacion: {camper[codCamper].get('Nro Identificacion')}
    Nombre: {camper[codCamper].get('Nombre')}
    Apellido: {camper[codCamper].get('Apellido')}
    Direccion: {camper[codCamper].get('Direccion')}
    Telefonos: {camper[codCamper].get('Telefonos')}
    Acudiente: {camper[codCamper].get('Acudiente')}
    Estado: {camper[codCamper].get('Estado')}
    ________________________
        """)
        
            print("¿Este es el camper que deseas eliminar?")
            print("1. Si")
            print("2. No")
            print("3. Salir")
            opc = int(input())
            if(opc == 1):
                camper.pop(codCamper)
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
        except StopIteration:
                print("ERROR. no se encuentra ese codigo")
    return "Camper deleted"

def menu():
    bandera = True
    while (bandera):
        print("""
    -----------------------------------------
    -             MENU CAMPER               -
    -----------------------------------------
    -     1. Ingresar Camper                -
    -     2. Editar Camper                  -
    -     3. Buscar Camper                  -
    -     4. Eliminar Camper                -
    -     0. Salir                          -
    -----------------------------------------
""")
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
                listarCamper()
            case 4:
                system("clear")
                borrar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)