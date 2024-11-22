"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
    a. Ingresar  una  fecha  desde  el  teclado,  verificando  que  corresponda  a  una  fecha 
    válida.
    b. Sumar N días a una fecha.
    c. Ingresar un horario desde teclado, verificando que sea correcto.
    d. Calcular  la  diferencia  entre  dos  horarios.  Si  el  primer  horario  fuera  mayor  al 
    segundo  se  considerará  que  el  primero  corresponde  al  día  anterior.  En  ningún 
    caso la diferencia en horas puede superar las 24 horas
"""
from typing import Tuple

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

def pedir_n() -> int:
    """Solicita un número positivo al usuario.
    Returns: 
        int: el número positivo.
    """
    try:
        n = int(input("Ingrese la cantidad de N días a sumar a la fecha: "))
        if n < 0:
            raise ValueError()
        return n
    except ValueError:
        print("Debe ingresar un entero positivo.")

def diasiguiente(fecha: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """Calcula la fecha siguiente a la fecha dada.
        Returns:
            tuple: retorna la fecha siguiente.
    """
    day, month, year = fecha
    dias = days_inmonth(month, year)

    day += 1
    if day > dias:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return (day, month, year)

def sumar_dias(n: int, fecha: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """Suma los días dados a la fecha recibida.
        Args: 
            n (int): debe ser un número entero positivo.
        Returns:
            list: retorna el día, mes y año sumados la cantidad 'n' de días.
    """
    for _ in range(n):
        fecha = diasiguiente(fecha)
    return fecha

def pedir_horario() -> Tuple[int, int]:
    """Solicita enteros que cumplan con el formato xx:xx y los devuelve.
    Returns:
        Tuple: tupla con los enteros en el formato hora, minutos.
    """
    while True:
        try:
            op = input("Ingrese un horaro separado por ':' (xx:xx) = ")
            hora_, min_ = map(int, (op).split(":"))
            break
        except ValueError:
            print("Debe ingresar enteros.")
    return hora_, min_

def validar_horario(hora_: int, min_: int) -> bool:
    """Valida si la hora y minutos dados son válidos.
    Args:
        hora_: entero que representa la hora.
        min_: entero que representa los minutos.
    Returns:
        bool: True si es una fecha válida, caso contrario False.
    """
    return 0 <= hora_ < 24 and 0 <= min_ < 60

def diferencia_horario(time1: Tuple[int, int], time2: Tuple[int, int]) -> Tuple[int, int]:
    """ Calcula la diferencia entre dos horarios y los devuelve en formato de tuplas.
    Args:
        time1: contiene hora y minutos del primer horario a sacar la diferencia.
        time2: contiene hora y minutos del segundo horario a sacar la diferencia.
    Returns:
        Tupla[int, int]: contiene la diferencia de horarios, el primer entero
        representando las horas y el segundo los minutos.
    """
    hora_1, min_1 = time1
    hora_2, min_2 = time2
    minutos1 = hora_1 * 60 + min_1
    minutos2 = hora_2 * 60 + min_2

    if minutos1 > minutos2:
        minutos2 += 1440

    diferencia = minutos2 - minutos1

    diferencia_hor = diferencia // 60
    diferencia_min = diferencia % 60

    return diferencia_hor, diferencia_min


def pedir_opc() -> int:
    """Muestra y solicita al usuario que lejia una de las opciones del menú.
    Args: None
    Returns:
        int: opción elegida.
    """
    opciones = {
        1: "Ingresar  una  fecha  desde  el  teclado,  verificando  que  corresponda  a  una  fecha válida",
        2: "Sumar N días a una fecha",
        3: "Ingresar un horario desde teclado, verificando que sea correcto",
        4: "Calcular la diferencia entre dos horarios. La diferencia en horas no puede superar las 24hs",
        5: "Salir del programa",
            }
    while True:
        print()
        for key, desc in opciones.items():
            print(f"{key}: {desc}")
        op = input("Elija una opción: ")
        try:
            op = int(op)
            if op in opciones:
                return op
        except ValueError:
            print("Debe ingresar un número válido.")


def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    while True:
        op = pedir_opc()

        match op:
            case 1:
                day, month, year = pedir_fecha()
                fecha = day, month, year
                if validar_fecha(*fecha):
                    print(f"La fecha que ingresó fue: {day}/{month}/{year} y es válida!")
                else:
                    print("Fecha inválida.")
            case 2:
                day, month, year = pedir_fecha()
                print(f"La fecha que ingresó fue: {day}/{month}/{year}")
                fecha = day, month, year
                n = pedir_n()
                if n and validar_fecha(*fecha):
                    day, month, year = sumar_dias(n, fecha)
                    print(f"La fecha con {n} {'dia' if n == 1 else 'días'} sumados es {day}/{month}/{year}")
                else:
                    print("No se pudo realizar la suma.")
            case 3:
                horas_, min_ = pedir_horario()
                if validar_horario(horas_, min_):
                    print("Horario válido !!")
                else:
                    print("Horario inválido !!")
            case 4:
                time1 = pedir_horario()
                time2 = pedir_horario()
                if validar_horario(*time1) and validar_horario(*time2):
                    dif_hora, dif_min = diferencia_horario(time1, time2)
                    print(f"La diferencia entre {time1} y {time2} es de {dif_hora}hs y {dif_min}min")
                else:
                    print("Horarios no válidos.")
            case 5:
                print("Adios!")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!!!")

# End-of-file (EOF)
