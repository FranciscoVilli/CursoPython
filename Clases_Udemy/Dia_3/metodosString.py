texto = "este es el texto federico"
resultado = texto.upper()       #pone todo en mayuscula
print(resultado)
resultado = texto.split()       #pone en forma de lista tomando por defecto el espacio
print(resultado)
resultado = texto.split("e")       #pone en forma de lista tomando la e como eapcio
print(resultado)

a = "Aprender"
b = "Python"
c = "Genial"

e = " ".join([a,b,c])
print(e)

resultado = texto.find("e")       #si no se encuentra sale -1
print(resultado)

resultado = texto.replace("este","hola")       #reemplazamos
print(resultado)

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(texto.replace("difícil","fácil").replace ("mala","buena"))