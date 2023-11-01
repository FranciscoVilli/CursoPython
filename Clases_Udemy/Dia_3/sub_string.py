#Slicing --> cortar en rodajas
texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:6]  #desde donde y hasta donde extraer
print(fragmento)
fragmento = texto[2:]  #desde donde y hasta el final
print(fragmento)
fragmento = texto[2:5:2]  #desde donde y hasta donde y en q multiplo
print(fragmento)

#invertimos
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])