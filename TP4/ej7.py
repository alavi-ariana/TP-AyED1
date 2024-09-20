""" Programa para eliminar  una  subcadena  de  una  cadena  de  caracteres,  a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante"""
def eliminar_subcadena_slice(cadena: str, start: int, carac: int) -> str:
    """ Eliminación de una subcadena de cadena a partir de posición start y
        de longitud carac con el uso de slices.
        Returns:
            str: la nueva cadena con la subcadena ya eliminada
    """
    return cadena[:start] + cadena[start + carac:]

def eliminar_subcadena_sinslice(cadena: str, start: int, carac: int) -> str:
    """ Eliminación de una subcadena de cadena a partir de posición start y
        de longitud carac sin uso de slices.
        Returns:
            str: la nueva cadena con la subcadena ya eliminada
    """
    resultado = ""
    for i, char in enumerate(cadena):
        if i < start or i >= start + carac:
            resultado += char
    return resultado

if __name__ == "__main__":
    try:
        op = input("Ingrese la frase: ")
        inicio, cant = map(int, input("Ingrese el inicio y cantidad de caracteres a eliminar (separados por coma): ").split(","))
        resultado_slice, resultado_noslice = eliminar_subcadena_slice(op, inicio, cant), eliminar_subcadena_sinslice(op, inicio, cant)
        print(f"Resultado con slice: {resultado_slice}")
        print(f"Resultado sin slice: {resultado_noslice}")
    except ValueError:
        print("Debe ingresar inicio y cantidad de caracteres")

# End-of-file (EOF)
