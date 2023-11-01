mi_lista = ["a","b","c"]
mi_lista2 = ["a","b","c"]
print(mi_lista)
print(len(mi_lista))
print(mi_lista[1])

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)



mi_lista3.append("hola") #Agrega al final
print(mi_lista3)
eliminado = mi_lista3.pop() #Elimina el fianl
print(mi_lista3)
print(eliminado)



lista = ['g','a','r','w','y']       #solo nos ayuda a ordenar pero no devuelve nada
lista.sort()                        #no se le puede almacenar en otra variable
print(lista)

lista.reverse()     #imprime en reversa
print(lista)