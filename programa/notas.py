from programa.camper import buscar

def incial():
    print("Ingrese las notas de las pruebas")
    teorica = int(input("Ingrese la nota teorica: "))
    practica = int(input("Ingrese la nota practica: "))
    promedio = (teorica + practica) / 2
    print(promedio)