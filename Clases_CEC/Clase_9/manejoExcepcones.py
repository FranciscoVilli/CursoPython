try:
    x = int(input("Ingresa un numero: "))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("No hay division para cero")



import math
x=float(input("Ingrese otro numero: "))
assert x>=0.0
x=math.sqrt(x)
print(x)