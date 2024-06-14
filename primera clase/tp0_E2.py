def validaAlumnos(matriz, alumnos, curso, comision):
    if matriz[curso][comision] + alumnos <= 30:
        return True
    else:
        return False

def cargaComisiones(matriz, cursos):
    alumnos = 0
    while alumnos != -1:
        print("Ingrese la cantidad de alumnos")
        alumnos = int(input())
        if alumnos != -1:
            curso = ingresa_valida(10000, 99999, "Ingrese el codigo del curso")
            posCurso = cursos.index(curso)
            comision = ingresa_valida(1, 15, "Ingrese la comision")
            if validaAlumnos(matriz, alumnos, posCurso, comision):
                matriz[posCurso][comision-1] += alumnos
            else:
                print("No hay cupo en la comision", comision, "del curso", curso)



def ingresa_valida(min, max, msg):
    data = int(input(msg))
    while data < min or data > max:
        data = int(input(msg))
    return data


def cargaCodigo(cursos):
    for i in range(10):
        print("Ingrese el codigo del curso", i+1)
        cursos[i] = int(input())
        while cursos[i] < 10000 or cursos[i] > 99999:
            print("El codigo debe ser de 5 digitos")
            print("Ingrese el codigo del curso", i+1)
            cursos[i] = int(input())


def muestraMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print()


#
def cursosMasCargados(matriz, cursos):
    valor = 0
    valores= []
    pos = []
    for f in range(len(matriz)):
        valor = max(matriz[f])
        if valor > 0:
            valores.append(valor)
            pos.append(matriz[f].index(valor))
            print("El curso", cursos[f], "tiene la comision", matriz[f].index(valor) + 1, "con", valor, "alumnos")
    print("El curso con mas alumnos es el", cursos[valores.index(max(valores))], "con", max(valores), "alumnos en la comision", pos[valores.index(max(valores))])
    print("")


def cursosPocosAlumnos(matriz, cursos):
    for f in range(len(matriz)):
        pos = []
        for c in range(len(matriz[f])):
            if matriz[f][c] <= 10:
                pos.append(c)
        print("El curso", cursos[f], "tiene las comisiones", pos, "con menos de 10 alumnos")
    print("")





def __main__():  # definimos la funcion main
    cursos = [0] * 10
    matriz = []
    filas = 10
    columnas = 15

    for f in range(filas):
        matriz.append([0]*columnas)

    #carga de cursos
    cargaCodigo(cursos)
    cargaComisiones(matriz, cursos)

    #muestra de los cursos sin alumnos (se puede hacer de mas formas pero serian muchos logs)
    muestraMatriz(matriz)
    print("-----------------------------")

    #muestra las comisiones con mas alumnos de cada curso
    cursosMasCargados(matriz, cursos)
    print("-----------------------------")
    #muestra las comisiones con menos de 10 alumnos de cada curso
    cursosPocosAlumnos(matriz, cursos)


if __name__ == "__main__":  # al hacer esto, le decimos que se ejecute automaticamente la funcion main al principio de ejecucion
    __main__()