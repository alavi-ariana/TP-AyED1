"""Escribir  una  función  que  reciba  como  parámetro  una  tupla  conteniendo  una  fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos,  los  que  serán  interpretados  según  un  año  de  corte  definido  dentro  del 
programa.  Cualquier  año  mayor  que  éste  se  considerará  del  siglo  pasado.  Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931".  Si  el  año  se  ingresa  en  cuatro  dígitos  el  año  de  corte  no  será  tenido  en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado."""
from typing import Tuple

def nombre_mes(num_mes: int) -> str:
    """Recibe un número y devuelve el mes asignado a ese número.
    Args:
        - num_mes(int): 
    """
    meses = {1: "Enero",
             2: "Febrero",
             3: "Marzo",
             4: "Abril",
             5: "Mayo",
             6: "Junio",
             7: "Julio",
             8: "Agosto",
             9: "Septiembre",
             10: "Octubre",
             11: "Noviembre",
             12: "Diciembre",}
    try:
        return meses[num_mes]
    except KeyError:
        return "Número sin mes asignado, no existe."


def validar_anio(year: int) -> int:
    """Devuele el año tomando en cuenta el año de corte.
    Args:
        year: año a validar.
    Returns:
        int: año válidado segpun el año corte.
    """
    anio_corte = 30
    if len(str(year)) <= 2:
        if year > anio_corte:
            year += 1900
        else:
            year += 2000
    return year

def es_bisiesto(year: int) -> bool:
    """ Verifica si el año es bisiesto o no.

        Returns: 
            bool: devuelve 'True' si el año cumple con las condiciones dichas de un año bisiesto,
        caso contrario devuelve 'False'.
    """
    return (year % 100 == 0 and year % 4 == 0 and year % 400 == 0) or (year % 4 == 0)

def days_inmonth(month: int, year: int) -> int:
    """Me devuelve la cantidad de días en el mes."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        return 29 if es_bisiesto(year) else 28
    return 30

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

def pedir_fecha() -> Tuple[int, int, int]:
    """Solicita al usuario enteros separados en / y si cumple el formato dia/mes/año la retorna.
    Args: 
        None
    Returns: 
        Tuple[int, int, int]: una tupla con los enteros asignados a day, month, year.
    """
    while True:
        try:
            op = input("Ingrese la fecha separada por '/' (day/month/xxxx)): ")
            day, month, year = map(int, op.split("/"))
            break
        except ValueError as e:
            print(e)
            print("Debe ingresar una fecha válida en el formato day/month/year.")
            continue
    return (day, month, year)

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    while True:
        op = input("¿Desea ingresar la fecha? (y/n): ")
        if op.lower() == "y":
            fecha = pedir_fecha()
            if validar_fecha(*fecha):
                day = fecha[0]
                month = nombre_mes(fecha[1])
                year = validar_anio(fecha[2])
                print(f"{day} de {month} de {year}")
            else:
                print("Fecha inválida.")
        else:
            print("adios :3 !")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE !!!")

# End-of-file (EOF)
