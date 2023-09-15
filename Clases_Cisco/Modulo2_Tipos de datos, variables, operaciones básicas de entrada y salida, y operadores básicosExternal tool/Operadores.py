# Los operadores básicos
# Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.

# Por ejemplo, como en la aritmética, el signo de + (más) es un operador el cual es capaz de sumar dos números, dando el resultado de la suma.

# Sin embargo, no todos los operadores de Python son tan simples como el signo de más, veamos algunos de los operadores disponibles en Python,
# las reglas que se deben seguir para emplearlos, y como interpretar las reglas que realizan.

# Se comenzará con los operadores que están asociados con las operaciones aritméticas más conocidas:

# +, -, *, /, //, %, **

# Operadores Aritméticos: exponenciación
# Un signo de ** (doble asterisco) es un operador de exponenciación (potencia).
# El argumento a la izquierda es la base, el de la derecha, el exponente.

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)


# Operadores Aritméticos: multiplicación
# Un símbolo de * (asterisco) es un operador de multiplicación.

# Ejecuta el código y revisa si la regla de entero frente a flotante aún funciona.

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Operadores Aritméticos: división
# Un símbolo de / (diagonal) es un operador de división.

# El valor después de la diagonal es el dividendo, el valor antes de la diagonal es el divisor.

# Ejecuta el código y analiza los resultados.

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


# El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.

# Esto es muy importante: el redondeo siempre va hacia abajo.


# Observa el código e intenta predecir el resultado nuevamente:

print(-6 // 4)
print(6. // -4)



# Operadores: residuo (módulo)
# El siguiente operador es uno muy peculiar, porque no tiene un equivalente dentro de los operadores aritméticos tradicionales.

# Su representación gráfica en Python es el símbolo de % (porcentaje), lo cual puede ser un poco confuso.

print(14 % 4)


# Operadores: suma
# El símbolo del operador de suma es el + (signo de más), el cual esta completamente alineado a los estándares matemáticos.

# De nuevo, observa el siguiente fragmento de código:

print(-4 + 4)
print(-4. + 8)



# El operador de resta, operadores unarios y binarios
# Por esta razón, el operador de resta es considerado uno de los operadores binarios, así como los demás operadores de suma, multiplicación y división.

# Pero el operador negativo puede ser utilizado de una forma diferente, observa la ultima línea de código del siguiente fragmento:

print(-4 - 4)
print(4. - 8)


# Entonces, si se sabe que la * tiene una mayor prioridad que la +, el resultado final debe de ser obvio.
2 + 3 * 5


# La mayoría de los operadores de Python tienen un enlazado hacia la izquierda,
# lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.

print(9 % 6 % 2)

# Lista de prioridades

# Prioridad	Operador	
# 1	+, -	unario
# 2	**	
# 3	*, /, //, %	
# 4	+, -	binario


# 8. Los operadores de exponenciación utilizan 
# enlazado del lado derecho, por ejemplo, 2 ** 2 ** 3 = 256.