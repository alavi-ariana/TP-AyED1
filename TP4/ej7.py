""" Programa para eliminar  una  subcadena  de  una  cadena  de  caracteres,  a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante"""
def eliminar_subcadena_slice(cadena: str, start: int, carac: int) -> str:
    """ Eliminación de una subcadena de cadena a partir de posición start y
        de longitud carac con el uso de slices.
        Args:
            - cadena(str): cadena original, no debe estar vacio.
            - start(int): posición inicial de dónde empezar a eliminar.
            - carac(int): cantidad de caracteres a eliminar desde la posición start.
        Returns:
            str: la nueva cadena con la subcadena ya eliminada
    """
    return cadena[:start] + cadena[start + carac:]

def eliminar_subcadena_sinslice(cadena: str, start: int, carac: int) -> str:
    """ Eliminación de una subcadena de cadena a partir de posición start y
        de longitud carac sin uso de slices.
        Args:
            - cadena(str): cadena original, no debe estar vacio.
            - start(int): posición inicial de dónde empezar a eliminar.
            - carac(int): cantidad de caracteres a eliminar desde la posición start.
        Returns:
            str: la nueva cadena con la subcadena ya eliminada
    """
    resultado = ""
    for i, char in enumerate(cadena):
        if i < start or i >= start + carac:
            resultado += char
    return resultado

if __name__ == "__main__":
    while True:
        try:
            op = input("Ingrese la frase: ")
            if op:
                inicio, cant = map(int, input("Ingrese el inicio y cantidad de caracteres a eliminar (separados por coma): ").split(","))
                break
            else:
                print("Debe ingresar algo.")
        except ValueError:
            print("Debe ingresar inicio y cantidad de caracteres")

    resultado_slice, resultado_noslice = eliminar_subcadena_slice(op, inicio, cant), eliminar_subcadena_sinslice(op, inicio, cant)
    print(f"Resultado con slice: {resultado_slice}")
    print(f"Resultado sin slice: {resultado_noslice}")
# End-of-file (EOF)
