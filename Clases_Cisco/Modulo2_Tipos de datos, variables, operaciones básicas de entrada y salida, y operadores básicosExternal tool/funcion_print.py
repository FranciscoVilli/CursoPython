# La barra invertida (\) tiene un significado muy especial cuando se usa dentro de las cadenas, es llamado el carácter de escape.

print("Hola\nmundo")   #\n salto de linea pero python toma como si fuera una sola linea

#por parte del lenguaje cuando ponemos una coma automaticamente nos da un espaciado

print("LaWitsiWitsiAraña" , "subió" , "asutelaraña.")


# El mecanismo se llama argumentos de palabra clave. 
# El nombre se deriva del hecho de que el significado de estos argumentos no se toma de su ubicación (posición) sino de la palabra 
# especial (palabra clave) utilizada para identificarlos.
# La función print() tiene dos argumentos de palabra clave que se pueden utilizar para estos propósitos.
# El primero de ellos se llama end.

print("Mi nombre es", "Python.",end=" ")        #une a los dos prints en una sola linea y ademas agrega un espacion mediante la palabra reservada end
print("Monty Python.")

# El argumento de palabra clave que puede hacer esto se denomina sep (separador)
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")    #en vez de los espacios se pone el separador que especifiquemos

# Ambos argumentos de palabras clave pueden mezclarse en una invocación, como aquí en la ventana del editor.