firstname = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
location = input("Ingrese su ubicacion: ")
age = int(input("Ingrese su edad: "))
if age >= 18 and age <= 65:
    print(f"Hola {firstname} {lastname} como tienes {age} años y vives en {location} eres el ganador de un auto 0 kilometros. Click en el siguiente enlace para recibir el premio")
elif age < 18 and age > 6:
    print(f"Hola {firstname} {lastname} como tienes {age} años y vives en {location} no eres acreedor del premio")
elif age <= 6:
    print(f"Hola {firstname} {lastname} como tienes {age} años todavia no debes utilizar celular")
else:
    print("No puedes acceder al premio")