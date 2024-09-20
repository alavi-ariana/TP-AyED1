""" Programa para imprimir por pantalla el calendario de un mes completo,
    correspondiente a un mes y año cualquiera basándose en la función suministrada.
"""
from tabulate import tabulate


def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """Función del profe..."""
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    century = anio // 100
    year2 = anio % 100
    diasem = (((26 * mes - 2)// 10)+ dia + year2 + (year2 // 4)+(century//4)-(2*century)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def es_bisiesto(y: int) -> bool:
    """ Verificación si el año es bisiesto.
        Return:
            bool: 'True' si el año es bisiesto, caso contrario 'False'
    """
    return (y % 100 == 0 and y % 4 == 0 and y % 400 == 0) or y % 4 == 0

def print_calendary(m: int, y: int) -> None:
    """Muestra el calendario completo de un mes y año determinados."""
    day_by_month = (31, 29 if es_bisiesto(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    first_day = diadelasemana(1, m, y)

    days_ina_week = ("DOM", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB")
    days_month = day_by_month[m - 1]

    calendary: list = []

    week = [''] * first_day

    for day in range(1, days_month + 1):
        week.append(day)
        if len(week) == 7:
            calendary.append(week)
            week = []

    if week:
        calendary.append(week + [''] * (7 - len(week)))

    print(tabulate(calendary, headers=days_ina_week, tablefmt='grid'))

def validez(m: int, y: int):
    """Se valida si el mes y año son válidos."""
    return m > 0 and m < 13 and y > 0

if __name__ == "__main__":
    while True:
        try:
            month = int(input("Ingrese el mes: "))
            year = int(input("Ingrese el año: "))
            if validez(month, year):
                break
            print("Fecha no válida.")
        except ValueError:
            print("Debe ingresar datos enteros positivos.")

    print_calendary(month, year)

# End-of-file (EOF)
