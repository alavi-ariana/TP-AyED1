""" Leer una cadena de caracteres e imprimirla centrada en pantalla.
    Suponer que la misma tiene 80 columnas."""

def capicua(cadena: str) -> None:
    """Determina si la cádena de caracteres es capicúa.
    Args:
        - cadena(str): La cadena no debe estar vacia.
    Returns:
        - None.
    """
    espacios = (80 - len(cadena)) // 2
    print(f"{' ' * espacios}{cadena}")

if __name__ == "__main__":
    strings_ = input("Ingrese la cadena de strings: ")
    if not strings_:
        print("Debe ingresar una cadena de strings.")
    else:
        capicua(strings_)

# End-of-file (EOF)
