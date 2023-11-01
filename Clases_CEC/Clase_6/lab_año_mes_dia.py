def es_bisiesto(anio):
    """
    Esta función toma un año como argumento y devuelve Verdadero si es bisiesto, o Falso de lo contrario.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def numero_de_dias(anio, mes):
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
        return None  

def dia_del_ano(anio, mes, dia):
    
    if anio < 1 or mes < 1 or mes > 12 or dia < 1:
        return None  

    max_dias_mes = numero_de_dias(anio, mes)

    if dia > max_dias_mes:
        return None  

    dia_del_anio = dia
    for m in range(1, mes):
        dias_del_mes = numero_de_dias(anio, m)
        dia_del_anio += dias_del_mes

    return dia_del_anio

print(dia_del_ano(2023, 1, 15))  
print(dia_del_ano(2023, 3, 10))  
print(dia_del_ano(2024, 12, 31))  
print(dia_del_ano(2023, 2, 30))  
print(dia_del_ano(2023, 13, 1))