aray = ["2569da66-90ea-4547-843d-f0c86beebb19",
"26632e30-ea04-4f7b-8f17-31559de0c710",
"35666123-4a95-4168-87b5-b2ba4ef794b3",
"3e9780b7-30c1-4039-b49c-0cddcb5efee5",
"2848249a-e53b-4f61-9c80-28c1353a5e0f"]

def cargar_arch():
    try:
        arch = open("list.txt", "wt")
        for i in range(aray.__len__()):
            arch.write("signal_id =" + "'" +aray[i] +"'"+ " or ")
        arch.close()
    except:
        print("Error desconocido")


def __main__():
    cargar_arch()

if __name__ == "__main__":
    __main__()
