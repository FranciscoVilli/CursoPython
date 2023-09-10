# Tipo de datos INT
print (type(23))
# Tipo de dato string
print(type("Francisco"))
# Tipo de dato bool
print(type(False))
# Tipo de datp float
print(type(34.6))

# Operadores
1<2 
1>2
1==2
1!=2
1>=2
# Variables
a = 4 + 2
print(a)
b = "Francisco"
print(a*b) #Solo en el caso del producto podemos duplicar el str las veces que especifiquemos en int

# Concatenacion
str1 = "Hola"
str2 = "EPN"
str3 = "Como estas"
space = " "
print(str1+str2+space+str3)
print(str1,str2,space,str3) #nos ayuda a utilizar diferentyes tipos de datos y de paso agrega una variable

# Convercion
x=5
print("El valor de x es: "+str(x))  #transforma solo en esta parte a string pero sigue siendo entero

#Numero de decimales
pi = 22/7
print("{:.4f}".format(pi))

#Lista   se puede modificar los valores
lista=[]  #pueden ser de diferente tipo y se puede almacenar de diferentes tipos
valores = [1,"hola",True]
print(valores)
print(valores[1])
print(valores[-3])  #empieza desde el final
del valores[1]      #elimina la posicion


listas = [1,2,3,4,5,6]
print(listas.count)
print(listas.index)
print(listas.pop)
print(listas.sort)
print(listas.reverse)
print(listas.extend)


#tupla   no se puede modificar
tupla = (1,"hola",3,23.5)
