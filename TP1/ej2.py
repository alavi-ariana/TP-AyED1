"""Programa para verificar si una fecha es válida."""
from typing import List

def es_fecha_valida(day: int, month: int, year: int) -> bool:
    """ Verifica la veracidad de la fecha ingresada en días, meses y años.

        Args:
            day (int): el día del mes.
            month (int): el mes del año.
            year (int): el año.
            
        Returns:
            bool: True si el día es válido y si el año es mayor a 0, caso contrario False.
    """
    fecha_valida = (
        months_31days(month, day) or
        months_30days(month, day) or
        february(day, year)
    )
    return fecha_valida and year > 0

def es_bisiesto(year: int) -> bool:
    """ Verifica si el año es bisiesto o no.

        Returns: 
            bool: devuelve 'True' si el año cumple con las condiciones dichas de un año bisiesto,
        caso contrario devuelve 'False'.
    """
    if (year % 100 == 0 and year % 4 == 0 and year % 400 == 0) or (year % 4 == 0):
        return True
    return False

def months_31days(month: int, day: int) -> bool:
    """ Verifica si el mes va a tener 31 días.
    
        Returns:
            bool: True si el día es válido en un mes con 31 días, False en caso contrario.
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return day > 0 and day < 32
    return False

def months_30days(month: int, day: int) -> bool:
    """Verifica si el mes va a tener 30 días."""
    if month in (4, 6, 9, 11):
        return day > 0 and day < 31
    return False

def february(day: int, year: int) -> bool:
    """ Dependiendo de si es bisiesto o no, va a validar la fecha con 28 o 29 días
        Returns:
            bool: True si la fecha coincide en el año, caso contrario False.
    """
    if es_bisiesto(year):
        return day > 0 and day < 30
    else:
        return day > 0 and day < 29

def main() -> None:
    """Permite al usuario ingresar la fecha a validar."""
    print("VERIFIQUE SI SU FECHA ES VÁLIDA")
    while True:
        try:
            day = int(input("Ingrese el día: "))
            month = int(input("Ingrese el mes: "))
            year = int(input("Ingrese el año: "))
            break
        except ValueError:
            print("Debe ingresar números enteros.")
            continue

    if es_fecha_valida(day, month, year):
        print(es_fecha_valida(day, month, year))
        print("Su fecha es válida.")
    else:
        print(es_fecha_valida(day, month, year))
        print("Fecha inválida.")


def verificar() -> None:
    """Verificación del comportamiento de la función 'es_fecha_valida'. """
    print("Fechas válidas:")
    show_boolean(fechas_validas)
    print("Fechas inválidas:")
    show_boolean(fechas_invalidas)

def show_boolean(lista: List[list[int]]) -> None:
    """Muestra la validez de las fechas en la lista dada.

    Args:
        lista (List[List[int]]): Lista de fechas, donde cada sublista contiene
                                días, meses y años en el mismo indice.
    """
    for i in range(len(lista[0])):
        day = lista[0][i]
        month = lista[1][i]
        year = lista[2][i]
        print(f"Fecha: {day}/{month}/{year} - Validez: {es_fecha_valida(day, month, year)}")


fechas_validas = [[29, 28, 31, 30, 1], [2, 2, 12, 6, 1], [2020, 2019, 2023, 2022, 2024],]
fechas_invalidas = [[29, 31, 32, 31, 30], [2, 4, 1, 6, 2], [2019, 2023, 2022, 2023, 2020],]

###Bloque principal
main()
print()
verificar()
#End-of-file (EOF)
