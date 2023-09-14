def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif numero <= 3:
        return True  # 2 y 3 son primos
    elif numero % 2 == 0 or numero % 3 == 0:
        return False  # Los múltiplos de 2 y 3 no son primos
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplo de uso:
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")