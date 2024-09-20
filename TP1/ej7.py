""" Este programa indica el día siguiente a la fecha otorgada. También permite sumarle días a la 
    fecha y calcular la cantidad de días existentes entre dos fechas cualesquiera"""

def days_inmonth(month: int, year: int) -> int:
    """Me devuelve la cantidad de días en el mes."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        return 29 if es_bisiesto(year) else 28
    return 30

def es_bisiesto(year: int) -> bool:
    """ Verificación si el año es bisiesto.
        Return:
            bool: 'True' si el año es bisiesto, caso contrario 'False'
    """
    return (year % 100 == 0 and year % 4 == 0 and year % 400 == 0) or year % 4 == 0

def diasiguiente(day: int, month: int, year: int) -> list:
    """Calcula la fecha siguiente a la fecha dada.
        Returns:
            list: retorna la fecha siguiente.
    """
    dias = days_inmonth(month, year)

    day += 1
    if day > dias:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return [day, month, year]

def sumar_dias(days: int, month: int, year: int, n: int) -> list:
    """Suma los días dados a la fecha recibida.
        Args: 
            n (int): debe ser un número entero positivo.
        Returns:
            list: retorna el día, mes y año sumados la cantidad 'n' de días.
    """
    fecha = [days, month, year]
    for _ in range(n):
        fecha = diasiguiente(*fecha)
    return fecha

def total_days(day: int, month: int, year: int) -> int:
    """Calcula los días total"""
    dias_totales = 0

    for y in range(year):
        dias_totales += 366 if es_bisiesto(y) else 365
    for m in range(1, month):
        dias_totales += days_inmonth(m, year)

    dias_totales += day
    return dias_totales

def diferencia_fechas(fecha1: tuple, fecha2: tuple) -> int:
    """
        Args: La fecha 1 debe ser anterior a la fecha 2."""
    days_date1 = total_days(*fecha1)
    days_date2 = total_days(*fecha2)
    return days_date2 - days_date1

def validar_fecha(day: int, month: int, year: int) -> bool:
    """Validación de la fecha.
        Returns:
            bool: 'True' si la fecha es válida entre los límites, caso contrario 'False.
    """
    if year < 0 or month < 1 or month > 12 or day < 1:
        return False
    if day > days_inmonth(month, year):
        return False
    return True

def fecha1_menor_fecha2(fecha1: tuple, fecha2: tuple) -> bool:
    """Se calcula si la fecha 1 es menor que la fecha 2."""
    day1, month1, year1 = fecha1
    day2, month2, year2 = fecha2
    return (day2, month2, year2) > (day1, month1, year1)

def opciones() -> None:
    """Muestro las opciones del menú."""
    op = ["Día siguiente a su fecha.",
        "Ingrese días a sumar a su fecha.",
        "Diferencia de días entre dos fechas.",]
    for i, items in enumerate(op):
        print(f"{i + 1}: {items}")

def main() -> None:
    """Se le pide al usuario qué programa desea ejecutar
        y las fechas necesarias para cada uno."""
    while True:
        opciones()
        op = input("Ingrese su opción: ")
        match op:
            case "1":
                try:
                    day = int(input("Ingrese el día: "))
                    month = int(input("Ingrese el mes: "))
                    year = int(input("Ingrese el año: "))
                    if validar_fecha(day, month, year):
                        fecha = diasiguiente(day, month, year)
                        print("FECHA SIGUIENTE")
                        print(f"{fecha[0]}/{fecha[1]}/{fecha[2]}")
                    else:
                        print("Debe ingresar una fecha válida.")
                except ValueError:
                    print("Debe ingresar enteros positivos.")
            case "2":
                try:
                    day = int(input("Ingrese el día: "))
                    month = int(input("Ingrese el mes: "))
                    year = int(input("Ingrese el año: "))
                    n = int(input("Cantidad de días a sumar: "))
                    if validar_fecha(day, month, year) and n > 0:
                        fecha = sumar_dias(day, month, year, n)
                        print("FECHA CON DÍAS SUMADOS")
                        print(f"{fecha[0]}/{fecha[1]}/{fecha[2]}")
                    else:
                        print("Debe ingresar datos válidos.")
                except ValueError:
                    print("Debe ingresar enteros positivos.")
            case "3":
                try:
                    print("PRIMERA FECHA.")
                    day = int(input("Ingrese día: "))
                    month = int(input("Ingrese mes: "))
                    year = int(input("Ingrese año: "))
                    print("SEGUNDA FECHA.")
                    day2 = int(input("Ingrese día: "))
                    month2 = int(input("Ingrese mes: "))
                    year2 = int(input("Ingrese año: "))
                    fecha1 = (day, month, year)
                    fecha2 = (day2, month2, year2)
                    validez = validar_fecha(*fecha1) and validar_fecha(*fecha2)
                    if fecha1_menor_fecha2(fecha1, fecha2) and validez:
                        resultado = diferencia_fechas(fecha1, fecha2)
                        print(f"{resultado} día/s")
                    else:
                        print("Debe ingresar una fecha válida.")
                except ValueError:
                    print("Debe ingresar enteros positivos.")



if __name__ == "__main__":
    main()

# End-of-file (EOF)
