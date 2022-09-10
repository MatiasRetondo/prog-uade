msg = "bro"
print(msg)


for i in range(1, 10):
    print(i)
    if i == 5:
        break
    print("hola")

#create function
def say_hello():
    print("hello")

say_hello()

#create a list
lista = [1, 2, 3, 4, 5]
lista.not_in(1) #return true if not in list
print(lista)

#create a file  
file = open("test.txt", "w")
file.write("Hola mundo")
file.close()

#read a file
file2 = open("test.txt", "r")
print(file2.read())
file2.close()

#read a file line by line

file3 = open("test.txt", "r")
for line in file3:
    print(line)
file3.close()

