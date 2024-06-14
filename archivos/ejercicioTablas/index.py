path = "archivos\\ejercicioTablas\\tabla-"
def tablaMultiplicar():
    try:
        num = int(input("Ingrese un numero entero entre 1 y 10: "))
        if num < 1 or num > 10:
            raise ValueError
        arch = open(path + str(num) + ".txt", "wt")
        for i in range(1, 11):
            arch.write(str(num) + " x " + str(i) + " = " + str(num * i) + "\n")
        arch.close()
    except ValueError:
        print("El numero ingresado no es valido")
    except OSError:
        print("Error: FIle not found on directory")
    except:
        print("Error desconocido")

def mostrarTabla():
    try:
        num = int(input("Ingrese un numero entero entre 1 y 10: "))
        if num < 1 or num > 10:
            raise ValueError
        arch = open(path + str(num) + ".txt", "rt")
        print(arch.read()) #si fuese un archivo mas grande, se podria usar un for para leer linea por linea
        arch.close()
    except ValueError:
        print("El numero ingresado no es valido")
    except (OSError, FileNotFoundError):
        print("Error: FIle not found on directory")
    except:
        print("Error desconocido")

def __main__():
    tablaMultiplicar()
    mostrarTabla()

if __name__ == "__main__":
    __main__()