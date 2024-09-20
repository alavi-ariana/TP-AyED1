""" Programa para reemplazar apariciones en una cadena"""
import re

def reemplazar_palabra(cadena: str, og: str, nuevo: str) -> tuple:
    """ Reemplaza todas las apariciones de una palabra en una cadena
        Returns:
            - tuple:
                str: nueva cadena con las palabras reemplazadas.
                int: cantidad de reemplazos realizados
    """
    patron = r'\b' + re.escape(og) + r'\b'
    nueva_cadena, contador = re.subn(patron, nuevo, cadena)
    return nueva_cadena, contador

if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    reemplazar = input("Ingrese palabra a reemplazar: ")
    reemplazo = input("Ingrese la nueva palabra: ")

    resultado, cant = reemplazar_palabra(frase, reemplazar, reemplazo)
    print(f"Cadena modificada: {resultado}")
    print(f"Cantidad de reemplazos realizados: {cant}")

# End-of-file (EOF)
