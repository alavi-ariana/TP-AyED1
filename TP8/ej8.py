from typing import Dict

def generar_dict() -> Dict:
    """Genera un diccionario en donde las claves son un entero entre el 1 y el 20 incluidos,
    y los valores son las claves al cuadrado.
    Returns:
        - Diccionario por comprensión con enteros.
    """
    return {x: x**2 for x in range(1, 21)}

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    diccionario = generar_dict()
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()

# End-of-file (EOF)
