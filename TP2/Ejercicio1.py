# Escribir  un  programa  que  permita  grabar  un  archivo  los  datos  de  lluvia  caída  du-rante un año. 
# Cada línea del archivo se grabará con el siguiente formato:<dia>;<mes>;<lluvia caída en mm>  por ejemplo  25;5;319
# Los  datos  se  generarán  mediante  números  al  azar,  asegurándose  que  las  fechas sean válidas. 
# La cantidad de registros también será un número al azar entre 50 y 200.  
# Por  último  se  solicita  leer  el  archivo  generado  e  imprimir  un  informe  en  for-mato matricial donde 
# cada columna represente a un mes y cada fila corresponda a los días del mes.
# Imprimir además el total de lluvia caída en todo el año.

import random

def generarArchivo():
    try:
        arch = open("TP2\\lluvia.txt", "wt")
        for i in range(random.randint(50, 200)):
            mes = random.randint(1, 12)
            if mes == 2:
                dia = random.randint(1, 28)
            elif mes in [4, 6, 9, 11]:
                dia = random.randint(1, 30)
            else:
                dia = random.randint(1, 31)
            lluvia = random.randint(0, 1000)
            arch.write(str(dia) + ";" + str(mes) + ";" + str(lluvia) + "\n")
        arch.close()
    except:
        print("Error desconocido")

def crearMatrizLluvia():
    matriz = []
    for i in range(12):
        matriz.append([])
        for j in range(31):
            matriz[i].append(0)
    return matriz

def imprimirInforme():
    try:
        arch = open("TP2\\lluvia.txt", "rt")
        matriz = crearMatrizLluvia()
        lluviaMax= 0
        for linea in arch:
            datos = linea.split(";")
            dia = int(datos[0])
            mes = int(datos[1])
            lluvia = int(datos[2])
            lluviaMax += lluvia
            matriz[mes - 1][dia - 1] = lluvia
        arch.close()
        print("Informe de lluvia caida en el año")
        print("Ene  Feb  Mar  Abr  May  Jun  Jul  Ago  Sep  Oct  Nov  Dic")
        for i in range(31):
            print(i + 1, end=" ")  # end=" " es para que no salte de linea 
            for j in range(12):
                print(matriz[j][i], end=" ")
            print()
        print("Lluvia maxima: ", lluviaMax, "mm")
    except:
        print("Error desconocido")

def __main__():
    generarArchivo()
    imprimirInforme()

if __name__ == "__main__":
    __main__()