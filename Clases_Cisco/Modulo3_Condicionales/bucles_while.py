# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)

# Intenta recordar cómo Python interpreta la verdad de una condición y ten en cuenta 
# que estas dos formas son equivalentes:

# while number != 0: y while number:

# La condición que verifica si un número es impar también puede codificarse en estas 
# formas equivalentes:

# if number % 2 == 1: y if number % 2:



# Por cierto, observa la función print(). La forma en que lo hemos utilizado aquí se 
# llama impresión multilínea. Puede utilizar comillas triples para imprimir cadenas en 
# varias líneas para facilitar
# la lectura del texto o crear un diseño especial basado en texto. Experimenta con ello.



print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")