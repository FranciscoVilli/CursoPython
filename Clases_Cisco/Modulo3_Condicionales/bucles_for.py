# Python a menudo viene con muchas funciones integradas que harán el trabajo por ti. 
# Por ejemplo, para encontrar el número más grande de todos, puede usar una función 
# incorporada de Python llamada max(). 
# Puedes usarlo con múltiples argumentos. 

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
largest_number = max(number1, number2, number3) #realiza el numero mas grande

# Imprime el resultado.
print("El número más grande es:", largest_number)

print(max(3,5,8,10))
# De la misma manera, puedes usar la función min() para devolver el número más pequeño.

print(min(3,5,8,10))