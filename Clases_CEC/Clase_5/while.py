numero = input("Ingrese el numero al que debo contar: ")
numero = int(numero)
contador=1
while contador <= numero:
    print(contador)
    contador+=1

numero = input("Ingrese el numero al que debo contar: ")
numero = int(numero)
contador=1
while True:
    print(contador)
    contador+=1
    if contador > numero:
        break