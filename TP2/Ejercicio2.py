#en la parte de los porcentajes (30% teoria y 40% prativa) se calcula asi:
# si las notas son: 7/7/8 (siendo 7 la nota de teoria y 8 la de practica) entonces:
# 7*0.3 + 7*0.3 + 8*0.4 = 7.4
import random
path = "TP2\\alumnos.txt"

def validaRecuperatorio(alumno):
    avaible = False
    count = 0
    if int(alumno["teoria1"]) < 4:
        count += 1
    if int(alumno["teoria2"]) < 4:
        count += 1
    if int(alumno["practica"]) < 4:
        count += 1
    if count > 0 and count < 2:
        avaible = True
    return avaible



def generarArchivo():
    alumno = {}
    try:
        arch = open(path, "wt")
        for i in range(10):
            alumno["nombre_apellido"] = "Alumno" + str(i)
            alumno["asistencia"] = str(random.randint(0, 100))
            alumno["teoria1"] = str(random.randint(1, 10))
            alumno["teoria2"] = str(random.randint(1, 10))
            alumno["practica"] = str(random.randint(1, 10))
            if validaRecuperatorio(alumno):
                alumno["recuperatorio"] = str(random.randint(1, 10))
            else:
                alumno["recuperatorio"] = "0"
            arch.write(alumno["nombre_apellido"] + "," + alumno["asistencia"] + "," + alumno["teoria1"] + "," + alumno["teoria2"] + "," + alumno["practica"] + "," + alumno["recuperatorio"])
            arch.write("\n")
        arch.close()
    except IOError:
        print("Error al escribir el archivo")
    except:
        print("Error inesperado")


#lee el archivo y ordena la lista por apellido
def informacionAlumnos(archivo):
    alumnos = []
    try:
        arch = open(archivo, "rt")
        for linea in arch:
            alumno = {}
            datos = linea.split(",")
            alumno["nombre_apellido"] = datos[0]
            alumno["asistencia"] = datos[1]
            alumno["teoria1"] = datos[2]
            alumno["teoria2"] = datos[3]
            alumno["practica"] = datos[4]
            alumno["recuperatorio"] = datos[5]
            alumnos.append(alumno)
        arch.close()
        alumnos.sort(key=lambda x: x["nombre_apellido"])
        return alumnos
    except FileNotFoundError:
        print("El archivo no existe")
    except:
        print("Error inesperado")


#calcula la nota final de cada alumno
def notaFinal(alumnos):
    for alumno in alumnos:
        try:
            notaTeoria = (int(alumno["teoria1"]) + int(alumno["teoria2"])) * 0.3
            notaPractica = int(alumno["practica"]) * 0.4
            notaRecuperatorio = int(alumno["recuperatorio"]) * 0.3 if int(alumno["teoria1"]) < 4 or int(alumno["teoria2"]) < 4 else int(alumno["recuperatorio"]) * 0.4
            alumno["notaFinal"] = notaTeoria + notaPractica + notaRecuperatorio
        except ValueError:
            print("Error en la nota de", alumno["nombre_apellido"])
        except:
            print("Error inesperado")
    return alumnos

#devuelve una lista con los alumnos aprobados y otra con los alumnos que deben recuperar
def aprobadosRecuperar(alumnos):
    aprobados = []
    recuperar = []
    for alumno in alumnos:
        if int(alumno["asistencia"]) >= 75:
            if int(alumno["teoria1"]) < 4 or int(alumno["teoria2"]) < 4 or int(alumno["practica"]) < 4:
                if int(alumno["recuperatorio"]) >= 4 and int(alumno["notaFinal"]) >= 5:
                    aprobados.append(alumno)
                else:
                    recuperar.append(alumno)
            else:
                if int(alumno["notaFinal"]) >= 5:
                    aprobados.append(alumno)
                else:
                    recuperar.append(alumno)
        else:
            recuperar.append(alumno)
    return aprobados, recuperar

def __main__():
    generarArchivo()
    alumnos = informacionAlumnos(path)
    alumnos = notaFinal(alumnos)
    aprobados, recuperar = aprobadosRecuperar(alumnos)
    print("APROBADOS")
    for alumno in aprobados:
        print(alumno)
    print("RECUPERAR")
    for alumno in recuperar:
        print(alumno)


if __name__ == "__main__":
    __main__()