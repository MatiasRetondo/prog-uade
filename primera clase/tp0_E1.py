from importlib.machinery import SourceFileLoader


def ingresa_valida(min, max, msg):
    data = int(input(msg))
    while data < min or data > max:
        data = int(input(msg))
    return data

def cargaUser(matriz):
    condicion = True
    values = []
    while condicion == True:
        print("Ingrtese numero de legajo")
        legajo = int(input())
        if legajo == 99999:
            condicion = False
        else:
            while legajo < 10000 or legajo > 25000 or legajo in values or legajo != 99999:
                print("El legajo debe estar entre 10000 y 25000")
                print("Ingrese el codigo del legajo")
                legajo = int(input())
            values.append(legajo)
            print("Ingrese el sueldo base")
            sueldo = int(input())
            while sueldo < 0:
                print("El sueldo debe ser mayor a 0")
                print("Ingrese el sueldo base")
                sueldo = int(input())
            values.append(sueldo)
            print("Ingrese la antiguedad")
            antiguedad = int(input())
            while antiguedad < 0:
                print("La antiguedad debe ser mayor a 0")
                print("Ingrese la antiguedad")
                antiguedad = int(input())
            values.append(antiguedad)
            print("Ingrese los dias de ausentismo")
            ausentismo = int(input())
            while ausentismo < 0:
                print("La ausentismo debe ser mayor o igual a 0")
                print("Ingrese los dias de ausentimo")
                ausentismo = int(input())
            values.append(ausentismo)
            print("Ingrese la cantidad de hijos")
            hijos = int(input())
            values.append(hijos)
            matriz.append(values)

            


def __main__():  # definimos la funcion main

    matriz = []
    cargaUser(matriz)
    print(matriz)

    





if __name__ == "__main__": 
    __main__()