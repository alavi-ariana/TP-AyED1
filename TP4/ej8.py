""" Devolver una subcadena con los últimos n caracteres de una cadena"""
def subcadena_n(cadena: str, n: int) -> str:
    """Uso de slice para devolver una subcadena de los ultimos n caracteres de una cadena
    Args:
        - cadena(str): cadena original, no debe estar vacio.
        - n(int): cantidad de caracteres a mostrar desde izq a der.
    Returns:
        - str: subcadena con los caracteres a mostrar.
    """
    return cadena[- n:]

if __name__ == "__main__":
    while True:
        try:
            cadena_op = input("Ingrese la frase: ")
            if cadena_op:
                n_op = int(input("Ingrese cantidad de últimos caracteres a mostrar: "))
                break
            else:
                print("Debe ingresar algo.")
        except ValueError:
            print("Ingrese un entero")
    print(subcadena_n(cadena_op, n_op))

# End-of-file (EOF)
