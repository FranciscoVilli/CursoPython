def es_bisiesto(anio):
    """
    Esta función toma un año como argumento y devuelve Verdadero si es bisiesto, o Falso de lo contrario.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def daysInMonth(anio, mes):
    """
    Esta función toma un año y un mes como argumentos y devuelve el número de días para ese mes en el año dado.
    """
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30_dias = [4, 6, 9, 11]

    if mes in meses_31_dias:
        return 31
    elif mes in meses_30_dias:
        return 30
    elif mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        return None  # Devolver None si el mes es inválido
    

testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")