"""Programa para determinar si una cadena de caracteres es capicúa"""
def capicua_str(cadena: str) -> bool:
    """ Determina si una cadena es capicúa sin el uso de cadenas auxiliares ni slices. 
    Args:
        - cadena(str): no debe estar vacio.
    Returns:
        - bool: True en el caso de que sí sea capicua, caso contrario False.
    """
    return all(a == b for a,b in zip(cadena, reversed(cadena)))

if __name__ == "__main__":
    cadena_op = input("Ingrese la cadena de caracteres: ")
    if not cadena_op:
        print("Debe ingresar algo.")
    else:
        print(f"{'Es' if capicua_str(cadena_op) else 'No es'} capicua.")

# End-of-file (EOF)
