def mensaje():
    print(int(input("ingrese un dato: ")))

mensaje()


#NO debe tener una funcion y una variable del mismo nombre

def saludo(nombre):
    print("FUncion saludo\n")
    print("HOla",nombre)

saludo("Fabian")

def direct(ciudad,barrio,calle="12 de Octubre"):
    print("Funcion Direccion\n")
    print("\nLa ciudad de entrega es: ",ciudad)
    print("El sector es: ",barrio)
    print("La calle es: ",calle)

ba = input("Ingrese el barrio: ")
ba = input("Ingrese la ciudad: ")
direct(ba,ba)


def resta(a,b):
    print("Funcion Resta\n")
    print(a-b)
resta(3,7)
resta(b=4,a=5)

def suma(a,b):
    print(a+b)
    return(a+b)
x = suma(3,5)
opt = x +1
print(opt)


def saludo2(lista):
    for i in lista:
        print("Hola,",i)
    print("")

saludo2(["Juan"])
saludo2(["Juan","Carlos","Ana"])
saludo2(["Juan","Carlos","Ana","Fabian"])
saludo2("Francisco")    #se imprime caracter por caraceter
saludo2(["Francisco"])  #Se imprime el nombre completo

def suma2(*a):
    print("\nTipo de datos del argumento:",type(a))
    sum = 0
    for n in a:
        sum +=n
    print("SUma:",sum)
suma2(1)
suma2(1,5,7,43,8)

#funciones lambda es anonima

