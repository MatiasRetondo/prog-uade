# es el ejercicio 3 de la guia

#generar un archivo de texto al que se le cargan un deporte y luego las alturas de los jugadores, se debe grabar en lineas distintas
#el deporte y las alturas de los jugadores

# generar promedio de las alturas de los jugadores por deporte

# mostrar por pantalla los deportes con altura promedio mayon a la altura promedio de todos los deportes
path = "archivos\ejercicio1.txt"
path2 = "archivos\ejercicio1Promedio.txt"

def cargaDeportesYAlturas():
    arch = open(path, "wt")
    var = input("Ingrese el deporte: ")
    while var != "-1":
        arch.write(var + "\n")
        var = input("Ingrese la altura: ")
        while var != "-1":
            arch.write(var + "\n")
            var = input("Ingrese la altura: ")
        var = input("Ingrese el deporte: ")
    arch.close()

def promedioAlturas():
    try:
        arch = open(path, "rt")
        arch2 = open(path2, "wt")
        var = arch.readline()
        while var != "":
            suma = 0
            cont = 0
            if not isFloat(var):
                arch2.write(var)
                var = arch.readline()
            else:
                while isFloat(var):
                    suma += float(var)
                    cont += 1
                    var = arch.readline()
                arch2.write(str(suma/cont) + "\n")
        arch.close()
        arch2.close()
        print("Archivo generado con exito")
    except OSError as err:
        print("Error: {0}".format(err))
        arch.close()
        arch2.close()

def isFloat(num):
    esflo = True
    try:
        float(num)
    except ValueError:
        esflo = False
    return esflo


def mostrarAlturasMayores():
    arch = open(path2, "rt")
    deportes = []
    alturas = []
    var = arch.readline()
    while var != "":
        deportes.append(var)
        var = arch.readline()
        alturas.append(float(var))
        var = arch.readline()
    arch.close()
    promedio = sum(alturas)/len(alturas)
    for i in range(len(alturas)):
        if alturas[i] > promedio:
            print(deportes[i], alturas[i])



def __main__():
    promedioAlturas()
    mostrarAlturasMayores()

if __name__ == "__main__":
    __main__()