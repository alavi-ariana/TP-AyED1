"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes  cuyo  número  se  recibe  como  parámetro.  Los  nombres  de  los  meses  deberán 
obtenerse  de  una  lista  de  cadenas  de  caracteres  inicializada  dentro  de  la  función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones"""
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

def main() -> None:
    """hola"""
    while True:
        try:
            num_mes = int(input("Ingrese número del mes: "))
            if num_mes > 0:
                break
            raise ValueError
        except ValueError:
            print("Debe ingresar valores válidos.")

    print(nombre_mes(num_mes))

if __name__ == "__main__":
    main()

# End-of-file (EOF)
