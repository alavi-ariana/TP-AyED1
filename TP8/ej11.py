from typing import Dict

def contarvocales(palabra: str) -> Dict:
    """Cuenta las vocales que se encuentran en una palabra.
    Args:
        palabra: la palabra a contar.
    Returns:
        Dict: un diccionario con cada vocal como clave y su valor es la cantidad de veces que aparece.
    """
    vocales = {"a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales

def leer_frase(frase: str) -> tuple:
    """Recibe una frase y palabra por palabra va contando la cantidad de vocales que tienen
        para al final devolver la sumatoria.
        Args:
            frase: string a contar palabra por palabra las letras.
        Returns:
            Tuple: todas las palabras de la frase, cantidad total de vocales en toda la frase.
        """
    total = 0
    palabras = frase.split()
    for palabra in palabras:
        resultado = contarvocales(palabra)
        total += sum(resultado.values())
    return palabras, total


def pedir_str() -> str:
    """Solicita al usuario un string."""
    return input("Ingrese su palabra: ")

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    palabrita = pedir_str()
    print(contarvocales(palabrita))
    frase = pedir_str()
    palabras, total = leer_frase(frase)
    print(f"{palabras} | total de vocales halladas: {total}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYEE !")

# End-of-file (EOF)
