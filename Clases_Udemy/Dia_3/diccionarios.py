#no tienen un orden de indice
diccionario = {"nombre":"Francisco",
               "apellido":"villalba",
               "edad":20}
print(type(diccionario))

resultado = diccionario["nombre"]
print(resultado)
print(diccionario)

dic = {"c1":55,"c2":[20,15,43]}
print(dic)
print(dic["c2"][2])

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2["c2"][1].upper())

diccionario = {"nombre":"Francisco",
               "apellido":"villalba",
               "edad":20}

diccionario[3]="hola"
print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())