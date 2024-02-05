import json

def carga():
    with open("programa/datosJson/modulos.json", "r") as f:
        return json.loads(f.read())