# realizar un programa para ingresar una frase y mostrar un listado ordenado alfabeticamente con las palabras que contiene,
# eliminando las repetidas y añadiendo la cantidad de veces que aparece cada una.


def ordenarPalabras():
    frase = input("Ingrese una frase: ")
    palabras = frase.split(" ")
    palabras.sort()
    return palabras

def formateoParaDic(palabras):
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    print("palabra  -> cantidad")
    claves = list(diccionario)
    claves.sort()
    for clave in claves:
        print(clave, "aparece :", diccionario[clave], "veces")
    # for palabra in diccionario:
    #     print(palabra, "->", diccionario[palabra])

def __main__():
    palabras = ordenarPalabras()
    formateoParaDic(palabras)

if __name__ == "__main__":  # al hacer esto, le decimos que se ejecute automaticamente la funcion main al principio de ejecucion
    __main__()
