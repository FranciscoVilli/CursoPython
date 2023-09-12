#Diccionarios

dic1 = {"R1":"10.10.1",
        "alumno":"Franciosco",
        "ID":1234}
print(dic1)
print(dic1["ID"])   #ya no imprimimos la posicion si no la clave

print("ap" in dic1)     #preguntamos si esque esxite una key llamada dic1
print("10.10.1" in dic1)     #preguntamos si esque esxite una key llamada dic1


#Entrada de datos
entrada = input("Escribe tu nombre: ")          #el input solo muestra strings y para almacenar una variable de numero se debe hacer la onversion a int
print(entrada)

numero = int(input("Digita tu edad"))
print(numero)
print(type(numero))