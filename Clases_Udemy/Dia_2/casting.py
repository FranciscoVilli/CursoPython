# Conversion implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2
print(num1)     #lo convierte a float

#Conversion explicita
num1 = 5.8
print(num1)
print(type(num1))

num2 = str(num1)
print(num2)
print(type(num2))


edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)

print("tu nueva edad es: " + str(nueva_edad))