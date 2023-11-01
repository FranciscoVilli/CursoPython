# Ejecución condicional: la sentencia if
# Si un determinado desarrollador de Python sin dormir se queda dormido cuando cuenta 120 ovejas,
# y el procedimiento de inducción del sueño se puede implementar como una función especial llamada 
# sleep_and_dream(), el código toma la siguiente forma:

# if sheep_counter >= 120: # #evalúa una expresión condicional
#     sleep_and_dream() #se ejecuta si la expresión condicional es True
	

# Puedes leerlo como sigue: si sheep_counter es mayor o igual que 120, entonces duerme y sueña 
# (es decir, ejecuta la función sleep_and_dream).

# Hemos dicho que las sentencias condicionales deben tener sangría. Esto crea una estructura muy
# legible, demostrando claramente todas las rutas de ejecución posibles en el código.

# Analiza el siguiente código:

# if sheep_counter >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()


# Como puedes ver, tender la cama, tomar una ducha y dormir y soñar se ejecutan condicionalmente, 
# cuando sheep_counter alcanza el límite deseado.

# Alimentar a los perros, sin embargo, siempre se hace (es decir, la función feed_the_sheepdogs()
# no tiene sangría y no pertenece al bloque if, lo que significa que siempre se ejecuta).

# Ahora vamos a discutir otra variante de la sentencia condicional, que también permite realizar 
# una acción adicional cuando no se cumple la condición.




# Ejecución condicional: la sentencia if-else
# Comenzamos con una frase simple que decía: Si el clima es bueno, saldremos a caminar.

# Nota: no hay una palabra sobre lo que sucederá si el clima es malo. Solo sabemos que no saldremos 
# al aire libre, pero no sabemos que podríamos hacer. Es posible que también queramos planificar algo 
# en caso de mal tiempo.

# Podemos decir, por ejemplo: Si el clima es bueno, saldremos a caminar, de lo contrario, iremos al cine.

# Ahora sabemos lo que haremos si se cumplen las condiciones, y sabemos lo que haremos si no todo sale 
# como queremos. En otras palabras, tenemos un "Plan B".

# Python nos permite expresar dichos planes alternativos. Esto se hace con una segunda forma, ligeramente
# mas compleja, de la sentencia condicional, la sentencia if-else:

# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false


# Por lo tanto, hay una nueva palabra: else - esta es una palabra clave reservada.

# La parte del código que comienza con else dice que hacer si no se cumple la condición especificada por
# el if (observa los dos puntos después de la palabra).

# La ejecución de if-else es la siguiente:

# Si la condición se evalúa como True (su valor no es igual a cero), la instrucción 
# perform_if_condition_true se ejecuta, y la sentencia condicional llega a su fin.
# Si la condición se evalúa como False (es igual a cero), la instrucción perform_if_condition_false
# se ejecuta, y la sentencia condicional llega a su fin.



# La sentencia elif
# El segundo caso especial presenta otra nueva palabra clave de Python: elif. Como probablemente 
# sospechas, es una forma más corta de else-if.

# elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera 
# sentencia verdadera.

# Nuestro siguiente ejemplo se parece a la anidación, pero las similitudes son muy leves. Nuevamente,
# cambiaremos nuestros planes y los expresaremos de la siguiente manera: si hay buen clima, saldremos a
# caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres 
# en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez.

# ¿Has notado cuantas veces hemos usado la palabra de lo contrario? Esta es la etapa en la que la palabra
# clave reservada elif desempeña su función.

# Escribamos el mismo escenario empleando Python:

# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()


x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("se ejecutará el else")


# Cada if se prueba por separado. 
# El cuerpo de else se ejecuta si el último if es False.