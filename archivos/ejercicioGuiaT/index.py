path = "archivos\\ejercicioGuiaT\\listado.txt"
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase #genera un caracter random de la a a la z
    result_str = ''.join(random.choice(letters) for i in range(length)) #genera un string de longitud length
    return result_str

# Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.

# El programa debe incorporar funciones crear el archivo con el listado si no existe, para consultar el teléfono de un cliente,
# añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
# El listado debe estar guardado en el archivo de texto listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas
# y cada cliente en una línea distinta. Utilizando excepciones, controlar que el usuario introduzca los datos correctos.

def crearArchivo():
    try:
        arch = open(path, "wt")
        arch.close()
    except FileExistsError:
        print("El archivo ya existe")
    except:
        print("Error desconocido")

def consultarTelefono():
    try:
        arch = open(path, "rt")
        nombre = input("Ingrese el nombre del cliente: ")
        for line in arch.readlines():
            if line.split(",")[0] == nombre:
                print("El telefono del cliente es: " + line.split(",")[1])
        arch.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except:
        print("Error desconocido")

def copiarArchivo():
    try:
        arch = open(path, "rt")
        archTemp = open("archivos\\ejercicioGuiaT\\listadoTemp.txt", "wt")
        for line in arch.readlines():
            archTemp.write(line)
        arch.close()
        archTemp.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except:
        print("Error desconocido")

def agregarTelefono():
    try:
        arch = open(path, "wt") #esto borraria el archivo y lo reescribiria con el nuevo cliente, deberia ser "at" pero no lo podemos usar. Deberia guardar la data en un archivo temporal y luego reescribir el archivo original
        archTemp = open("archivos\\ejercicioGuiaT\\listadoTemp.txt", "wt")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        for line in arch.readlines():
            archTemp.write(line)
        arch.write(nombre + "," + telefono + "\n")
        arch.close()
        archTemp.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except:
        print("Error desconocido")


def eliminarTelefono():
    try:
        arch = open(path, "rt")
        archTemp = open("archivos\\ejercicioGuiaT\\listadoTemp.txt", "wt")
        nombre = input("Ingrese el nombre del cliente: ")
        for line in arch.readlines():
            if line.split(",")[0] != nombre:
                archTemp.write(line)
        arch.close()
        archTemp.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except:
        print("Error desconocido")
def __main__():
    print("Bienvenido al sistema de archivos")

if __name__ == "__main__":
    __main__()