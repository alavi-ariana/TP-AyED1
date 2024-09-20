""" Leer una cadena de caracteres e imprimirla centrada en pantalla.
    Suponer que la misma tiene 80 columnas."""

if __name__ == "__main__":
    cadena = input("Ingrese la cadena de strings: ")
    espacios = (80 - len(cadena)) // 2
    print(f"{' ' * espacios}{cadena}")

# End-of-file (EOF)
