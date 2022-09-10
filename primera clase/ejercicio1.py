# datos que tenemos primer paralelismo: categoria, importe y valores 
# datos que tenemos segundo paralelismo: num_registro, categoria y año 

def ingresa_valida(min, max, msg):
    data = input(msg)
    while data < min or data > max:
        data = int(input(msg))
    return data

def leecategoria():
    categorias = ["A", "B", "C", "D", "E", "F"]
    print("ingrese una categoria")
    categoria = input()
    while categoria not in categorias:
        print("ingrese una categoria valida")
        categoria = input()
    return categoria

def busqueda(lista, valor):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == valor:
            pos = i
        i += 1
    return pos

def cargar_registros(num_registros, categorias_autos, años_autos):
    max = 900
    #while num_registros < max and categorias_autos != F load data
    while len(num_registros) < max and categorias_autos != "F":
        num_registros.append(ingresa_valida(4, 6, "ingrese numero de registro"))
        categorias_autos.append(leecategoria())
        años_autos.append(ingresa_valida(1975, 1990, "ingrese año"))



#creamos funcion main para que se ejecute el programa
def main():
    categorias = ["A", "B", "C", "D", "E"]
    importes = [10000, 12000, 13000, 14000, 15000]
    valores = [0]*5

    años_autos = []
    num_registros = []
    categorias_autos = []

    cargar_registros(num_registros, categorias_autos, años_autos)

    
    