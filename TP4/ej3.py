"""Ibtencipon de clavez 1 y claves 2 de la clave maestrta"""
def claves(maestra: str) -> tuple:
    """ Divide una cadena maestra en dos claves, extrayendo caracteres en
        posiciones pares e impares
        Args:
            - maestra str: se espera que la cadena no esté vacia
        Returns:
            - tuple:
                clave1: contiene los caracteres pares de la cadena maestra
                clave2: contiene los caracteres en impares de la cadena maestra
    """
    return maestra[::2], maestra[1::2]

if __name__ == "__main__":
    llave_maestra = input("Ingrese la clave maestra: ")
    if not llave_maestra:
        print("Debe ingresar algo.")
    else:
        clave_1, clave_2 = claves(llave_maestra)
        print(f"Clave 1: {clave_1} - Clave 2: {clave_2}")

# End-of-file (EOF)
