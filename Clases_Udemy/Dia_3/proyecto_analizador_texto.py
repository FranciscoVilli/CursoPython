print("--------Analizador de texto-------")
print("                  ||              ")
print("                  ||              ")
print("                  ||              ")
print("                  ↓↓              ")
texto = input("Ingresa un texto cualquiera \n\n")
print("\n")
letras = []

texto = texto.lower()
letras.append(input("Ingresa la primer letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
print("\nResultado....")
print("#######################\n")

print("Cantidad de letras\n")
cantidad_letras = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetido {cantidad_letras} veces")
print(f"Hemos encontrado la letra {letras[1]} repetido {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetido {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras\n")

cantidad_palabras = texto.split()
resultado = len(cantidad_palabras)
#print(cantidad_palabras)
print(f"La cantidad de palabras encontradas es: {resultado} palabras")
print("\n")

print("Letra de inicio y fin\n")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicio es '{letra_inicio}' y la letra final es '{letra_fin}'")

print("\n")

print("Texto invertido\n")
cantidad_palabras.reverse()
texto_invertido = ' '.join(cantidad_palabras)
print(f"El texto invertido quedaria asi: {texto_invertido}\n")

print("Buscando.... la Palabra Pytohn\n")
buscar_python = 'python'in texto
dic = {True:"si",False:"no"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")




