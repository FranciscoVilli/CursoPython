class MiPrimeraClase:
    pass
object1 = MiPrimeraClase()
object2 = MiPrimeraClase()
object3 = MiPrimeraClase()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Nombre: {self.name}")
        print(f"Salario: ${self.salary}")

# Ejemplo de uso:
employee1 = Employee("Juan Pérez", 50000)
employee1.display_info()
