""" Programa para reemplazar apariciones en una cadena"""
import re

def reemplazar_palabra(cadena: str, og: str, nuevo: str) -> tuple:
    """ Reemplaza todas las apariciones de una palabra en una cadena
        Args:
            - cadena(str): cadena original, no debe estar vacio.
            - og(str): la palabra original a reemplazar.
            - nuevo(str): la nueva palabra con la que reemplazar a la original.
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
    if frase and reemplazar and reemplazo:
        resultado, cant = reemplazar_palabra(frase, reemplazar, reemplazo)
        print(f"Cadena modificada: {resultado}")
        print(f"Cantidad de reemplazos realizados: {cant}")
    else:
        print("Debe ingresar valores válidos.")

# End-of-file (EOF)
