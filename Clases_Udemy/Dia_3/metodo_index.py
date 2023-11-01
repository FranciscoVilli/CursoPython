#Los signos y los espacios ocupan espacios
texto = "hola como estas"
resul = texto[0]
print(resul)

resul2 = texto.index("o")
print(resul2)

resul3 = texto.index("o",2,7)  #desde donde y hasta donde
print(resul3)

resul4 = texto.rindex("o")  #busca de derecha a izquierda
print(resul4)