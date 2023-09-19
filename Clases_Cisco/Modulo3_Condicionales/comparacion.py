# Para hacer esta pregunta, se utiliza el == operador (igual igual).

# No olvides esta importante distinción:

# = es un operador de asignación, por ejemplo, a = b assigna a la varable a el valor de b.
# == es una pregunta ¿Son estos valores iguales? así que a == b compara a y b.



# Desigualdad: el operador no es igual a (!=)
# El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia: 
# si son iguales, el resultado de la comparación es False. 
# Si no son iguales, el resultado de la comparación es True.


# Operadores de comparación: mayor que
# También se puede hacer una pregunta de comparación usando el operador > (mayor que).

# Si deseas saber si hay más ovejas negras que blancas, puedes escribirlo de la siguiente manera:

# black_sheep > white_sheep  # mayor que


# True lo confirma; False lo niega.


# Operadores de comparación: mayor o igual que
# El operador mayor que tiene otra variante especial, una variante no estricta, pero se denota de manera diferente que la notación aritmética clásica: >= (mayor o igual que).

# Hay dos signos subsecuentes, no uno.

# Ambos operadores (estrictos y no estrictos), así como los otros dos que se analizan en la siguiente sección, son operadores binarios con enlace del lado izquierdo, y su prioridad es mayor que la mostrada por == y !=.

# Si queremos saber si tenemos que usar un gorro o no, nos hacemos la siguiente pregunta:

# centigrade_outside ≥ 0.0  # mayor o igual que


# Operadores de comparación: menor o igual que
# Como probablemente ya hayas adivinado, los operadores utilizados en este caso son: El operador < (menor que) y su hermano no estricto: <= (menor o igual que).

# Observa este ejemplo simple:

# current_velocity_mph < 85  # Menor que
# current_velocity_mph ≤ 85  # Menor o igual que



# Prioridad	Operador	
# 1	+, -	unario
# 2	**	
# 3	*, /, //, %	
# 4	+, -	binario
# 5	<, <=, >, >=	
# 6	==, !=