path = "archivos\\ejercicioPrecios\\"
import random
import string

rubros = ["Perfumeria", "Limpieza", "Maquillaje"]
def get_random_string(length):
    letters = string.ascii_lowercase #genera un caracter random de la a a la z
    result_str = ''.join(random.choice(letters) for i in range(length)) #genera un string de longitud length
    return result_str

def generaPrecios():
    try:
        arch = open(path + "precios.txt", "wt")
        for i in range(random.randint(10, 20)):
            new_str = get_random_string(8)
            robro = random.choice(rubros)
            arch.write(str(i) + ";" +  new_str  + ";" + robro + ";" + str(i) + "\n")
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

def nuevosPrecios():
    try:
        arch = open(path + "precios.txt", "rt")
        archP = open(path + "preciosP.txt", "wt")
        archL = open(path + "preciosL.txt", "wt")
        archM = open(path + "preciosM.txt", "wt")
        maxPricex = ""
        maxPrice = 0
        for line in arch.readlines():
            splitLine = line.split(";")
            if splitLine[2] == "Perfumeria":
                archP.write(splitLine[0] + ";" + splitLine[1] + ";" + str(float(splitLine[3]) * 1.1) + "\n")
            elif splitLine[2] == "Limpieza":
                archL.write(splitLine[0] + ";" + splitLine[1] + ";" + str(float(splitLine[3]) * 1.2) + "\n")
            elif splitLine[2] == "Maquillaje":
                archM.write(splitLine[0] + ";" + splitLine[1] + ";" + str(float(splitLine[3]) * 1.5) + "\n")
                #find max price in Maquillaje
                if float(splitLine[3]) * 1.5 > maxPrice:
                    maxPrice = float(splitLine[3])  * 1.5
                    maxPriceName = splitLine[1]
        print("El producto mas caro de Maquillaje es: " + maxPriceName + " con un precio de: " + str(maxPrice))
        arch.close()
        archP.close()
        archL.close()
        archM.close()
    except ValueError:
        print("El numero ingresado no es valido")
    except OSError:
        print("Error: FIle not found on directory")
    except:
        print("Error desconocido")

def __main__():
    generaPrecios()
    acumular20p()
    nuevosPrecios()



if __name__ == "__main__":
    __main__()