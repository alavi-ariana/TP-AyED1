""" Programa"""
def subcadena_slice(cadena: str, start: int, caracteres: int) -> str:
    """ Creción de una subcadena de una cadena utilizando slices.
    Args:
        - cadena(str): cadena de la que substraer subcadenas.
        - start(int): inicio de la partición de la cadena original.
        - caracteres(int): cantidad de caracteres a substraer desde la posición inicial.
    Returns:
        - str: el resultado de las subcadena.
    """
    return cadena[start:start + caracteres]

def subcadena_sinslice(cadena:str, start:int, caracteres:int) -> str:
    """ Creción de una subcadena de una cadena sin utilizar slices.
    Args:
        - cadena(str): cadena de la que substraer subcadenas.
        - start(int): inicio de la partición de la cadena original.
        - caracteres(int): cantidad de caracteres a substraer desde la posición inicial.
    Returns:
        - str: el resultado de las subcadena.
    """
    subcadena = ""
    for i in range(start, start + caracteres):
        if i < len(cadena):
            subcadena += cadena[i]
    return subcadena

if __name__ == "__main__":
    try:
        op, inicio, carac = input("Ingrese la frase, inicio y caracteres separando por comas: ").split(",")
        inicio = int(inicio)
        carac = int(carac)
        resultado_slice, resultado_sinslice = subcadena_slice(op, inicio, carac), subcadena_sinslice(op, inicio, carac)
        print(f"Resultado con slice: {resultado_slice}")
        print(f"Resultado sin slice: {resultado_sinslice}")
    except ValueError:
        print("Asegurese de ingresar la frase, el inicio y la cantidad de caracteres")
