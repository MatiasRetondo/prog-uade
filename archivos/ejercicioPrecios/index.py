path = "archivos\\ejercicioPrecios\\"
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase #genera un caracter random de la a a la z
    result_str = ''.join(random.choice(letters) for i in range(length)) #genera un string de longitud length
    return result_str

def generaPrecios():
    try:
        arch = open(path + "precios.txt", "wt")
        for i in range(random.randint(10, 20)):
            new_str = get_random_string(8)
            new_str2 = get_random_string(8)
            arch.write(str(i) + ";" +  new_str  + ";" + new_str2 + ";" + str(i) + "\n")
        arch.close()
    except OSError:
        print("Error: FIle not found on directory")
    except:
        print("Error desconocido")

def acumular20p():
    try:
        arch = open(path + "precios.txt", "rt")
        arch2 = open(path + "precios2.txt", "wt")
        for line in arch.readlines():
            line = line.split(";")
            line[3] = str(float(line[3]) * 1.2) + "\n"
            arch2.write(";".join(line))
        arch.close()
        arch2.close() 
    except ValueError:
        print("El numero ingresado no es valido")
    except OSError:
        print("Error: FIle not found on directory")
    except:
        print("Error desconocido")


def __main__():
    acumular20p()
    generaPrecios()



if __name__ == "__main__":
    __main__()