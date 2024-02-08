import json
from os import system
from .datos import trainer
from .valido import menuNoValid

def guardar():
    print("""
        *******************
        * Guardar Trainer *
        *******************
        """)
    info = {
        "Nro Identificacion": input("Ingrese el numero de identificacion: "),
        "Nombre completo": input("Ingrese el nombre completo: ")
    }
    trainer.append(info)
    with open("programa/datosJson/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Trainer"

def buscar():
    system("clear")
    print(f"""
    *******************
    *  Buscar Trainer  *
    *******************
    """)
    for i,val in enumerate(trainer):
        print(f"""
    ____________________________
    Codigo: {i}
    Nro Identificacion: {val.get('Nro Identificacion')}
    Nombre completo: {val.get('Nombre completo')}
    ____________________________
        """)
    return "El camper esta disponible"

def asignarCamper():
    with open("programa/datosJson/camper.json", "r") as f:
        campers = json.loads(f.read())
        f.close()
    codruta = int(input("Codigo de ruta: "))
    print(f"{campers[codruta]}")
    with open("programa/datosJson/modulo.json", "r") as f:
        modulos = json.loads(f.read())
        f.close()
    while True:
        codmod = int(input("Codigo de modulo: "))
        print(modulos[codmod])
        rutas[codruta]["Modulo"].append(modulos[codmod])
        with open("programa/datosJson/ruta.json", "w") as f:
            rutas = json.dumps(rutas, indent=4)
            f.write(rutas)
            f.close()
        opc = int(input("Quieres asigar otro modulo?\n1.Si\n2.No\n "))
        if opc == 1:
            asigarmodulo()
        elif opc == 2:
            system("clear")
            print("Modulo asignado correctamente")
            break
        
def menu():
    bandera = True
    while (bandera):
        print("""
        ****************
        * Menu Trainer *
        *****************
        """)
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t0. Atras")
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
                buscar()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)