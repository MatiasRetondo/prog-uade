from importlib.machinery import SourceFileLoader

def calculoBase(matriz):
    #10% del sueldo base si ausentismos es igual a 0
    #5% del sueldo base por cada hijo
    arraySueldo = []
    for i in range(len(matriz)):
        sueldo = matriz[i][1]
        if matriz[i][2] >= 15:
            sueldo += (sueldo * 0.12)
        ausentismo = matriz[i][3]
        hijos = matriz[i][4]
        if ausentismo == 0:
            sueldo += (sueldo * 0.1)
        sueldo += (hijos * (sueldo * 0.05))
        arraySueldo.append(sueldo - matriz[i][1])
        matriz[i][1] = sueldo
        print("la base imponible de:" + str(matriz[i][0]) + " es de: " + str(arraySueldo[i]))
    return arraySueldo

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

            
def muestraMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print()

def muestraMatrizParalela(matriz, arraySueldo):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print("Legajo: " + str(matriz[f][0]) + " Sueldo: " + str(matriz[f][1]) + " Base Imponible: " + str(arraySueldo[f]))


def calculaPromedioArray(array):
    promedio = 0
    for i in range(len(array)):
        promedio += array[i]
    promedio = promedio / len(array)
    return promedio

def calculoMedicina(matriz, arraySueldo):
    medicina = []
    valor = 0
    for f in range(len(matriz)):
        valor = arraySueldo[f] * 0.07
        medicina.append(valor)
        print("el total a pagar de medicina de Legajo: " + str(matriz[f][0]) + " es de: " + str(valor))
        if matriz[f][2] < 15:
            matriz[f][1] = matriz[f][1] - valor
    print("El total a pagar de medicina es de: " + str(sum(medicina)))
    print("El promedio a pagar de medicina es de: " + str(calculaPromedioArray(medicina)))

    
def orderAndSlice(matriz):
    arraySueldo = []
    arrayAntiguedad = []
    for i in range(len(matriz)):
        arraySueldo.append(matriz[i][1])
        arrayAntiguedad.append(matriz[i][2])
    for i in range(len(arraySueldo)):
        for j in range(len(arraySueldo)):
            if arrayAntiguedad[i] < arrayAntiguedad[j]:
                aux = arraySueldo[i]
                arraySueldo[i] = arraySueldo[j]
                arraySueldo[j] = aux
                aux = arrayAntiguedad[i]
                arrayAntiguedad[i] = arrayAntiguedad[j]
                arrayAntiguedad[j] = aux
    if (len(arraySueldo) % 2) == 0:
        mitad = int(len(arraySueldo) / 2)
        print("Los sueldos con mayor antiguedad son ", arraySueldo[:mitad])
        print("Los sueldos con menor antiguedad son ", arraySueldo[mitad:])
        
                

def __main__():  # definimos la funcion main

    matriz = []
    arraySueldo = []
    cargaUser(matriz)
    print(matriz)

    #Punto 2 - Calculo de sueldo base
    arraySueldo = calculoBase(matriz)
    muestraMatrizParalela(matriz, arraySueldo)

    #Puntos 3 y 4 - Calculo medicina prepaga y promedio de gasto medicina
    calculoMedicina(matriz, arraySueldo)
    





if __name__ == "__main__": 
    __main__()