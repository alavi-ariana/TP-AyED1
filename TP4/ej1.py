"""Programa para determinar si una cadena de caracteres es capicúa"""
def capicua_str(cadena: str) -> bool:
    """ Determina si una cadena es capicúa. """
    return all(a == b for a,b in zip(cadena, reversed(cadena)))

if __name__ == "__main__":
    cadena_op = input("Ingrese la cadena de caracteres: ")

    print(f"{'Es' if capicua_str(cadena_op) else 'No es'} capicua.")

# End-of-file (EOF)
