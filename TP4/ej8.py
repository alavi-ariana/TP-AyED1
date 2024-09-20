""" Devolver una subcadena con los últimos n caracteres de una cadena"""
def subcadena_n(cadena: str, n: int) -> str:
    """Uso de slice para devolver una subcadena de los ultimos n caracteres de una cadena"""
    return cadena[- n:]

if __name__ == "__main__":
    try:
        cadena_op = input("Ingrese la frase: ")
        n_op = int(input("Ingrese cantidad de últimos caracteres a mostrar: "))
        print(subcadena_n(cadena_op, n_op))
    except ValueError:
        print("Ingrese un entero")

# End-of-file (EOF)
