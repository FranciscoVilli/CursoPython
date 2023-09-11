
#ENTEROS

# Enteros, es decir, aquellos que no tienen una parte fraccionaria.
# Y números punto-flotantes (o simplemente flotantes), los cuales contienen (o son capaces de contener) una parte fraccionaría.

# Por lo tanto, el número se puede escribir ya sea así: 11111111, o como sigue: 11_111_111.
#  ¿Qué es lo que Python permite? El uso de guion bajo en los literales numéricos.

print(1_1_1_1_3)    #en consola se mostrara solo los numeros

# Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. 
# Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

print(0o123)    #la funcion print traduce el numero a octal

# La segunda convención nos permite utilizar números en hexadecimal.
# Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).

print(0x123)    #Lo mismo sucede con hexadecimal


#FLOTANTES
    # Ahora es tiempo de hablar acerca de otro tipo, el cual esta designado para representar y 
    # almacenar los números que (como lo diría un matemático) tienen una parte decimal no vacía.

    # Son números que tienen (o pueden tener) una parte fraccionaria después del punto decimal,
    # y aunque esta definición es muy pobre, es suficiente para lo que se desea discutir.

# el número no contenga comas.
# Pero no hay que olvidar esta sencilla regla, se puede omitir el cero cuando es el único dígito antes del punto decimal.

# En esencia, el valor 0.4 se puede escribir como:

print(.4)

# Por ejemplo: el valor de 4.0 puede ser escrito como:

print(.4)

# Esto no cambiará su tipo ni su valor.

# Cuando se desea utilizar números que son muy pequeños o muy grandes, se puede implementar la notación científica.

# Por ejemplo, la velocidad de la luz, expresada en metros por segundo. Escrita directamente se vería de la siguiente manera: 300000000.

# Para evitar escribir tantos ceros, los libros de texto emplean la forma abreviada, la cual probablemente hayas visto: 3 x 108.

print(3E8)

# Cuando se corre en Python:

print(0.0000000000000000000001)

# Python siempre elige la presentación más corta del número, y esto se debe de tomar en consideración al crear literales.


#CADENAS


# Las cadenas se emplean cuando se requiere procesar texto (como nombres de cualquier tipo, direcciones, novelas, etc.), no números.

# Ya conoces un poco acerca de ellos, por ejemplo, que las cadenas requieren comillas así como los flotantes necesitan punto decimal.

# La primera se basa en el concepto ya conocido del carácter de escape, 
# el cual recordarás se utiliza empleando la diagonal invertida. La diagonal
# invertida puede también escapar de la comilla. Una comilla precedida por una 
# diagonal invertida cambia su significado, no es un limitador, simplemente es una comilla. 
# Lo siguiente funcionará como se desea:

print("Me gusta \"Monty Python\"")

print('Me gusta "Monty Python"')        #en esete ejemplo no se utiliza el scape ya que estamos usando al principio comillas simples

    #Valores Booleanos

# Para concluir con los literales de Python, existen dos más.

# No son tan obvios como los anteriores y se emplean para representar
# un valor muy abstracto - la veracidad.

# Cada vez que se le pregunta a Python si un número es más grande que otro, 
# el resultado es la creación de un tipo de dato muy específico - un valor booleano.

# El nombre proviene de George Boole (1815-1864), el autor de Las Leyes del Pensamiento,
# las cuales definen el Álgebra Booleana - una parte del álgebra que hace uso de dos valores: Verdadero y Falso, denotados como 1 y 0.

True
False

# No se pueden cambiar, se deben tomar estos símbolos como son, incluso respetando las mayúsculas y minúsculas.