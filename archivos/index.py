# El campo ; separa los campos dentro del registro
# El campo \n separa los registros dentro del archivo
#Vamos a manejar archivos de TEXTO

try:
    arch = open("ejemplo.txt", "r")
    print(arch.read())
except IOError as err:
    print("Error: {0}".format(err))
except OSError as err:
    print("Error: {0}".format(err))
except:
    print("Error desconocido")
finally:
    arch.close()