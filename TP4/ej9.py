""" Programa"""
import re

def palabras_ordenadas(cadena: str) -> str:
    """ Ordena las palabras de la cadena según su longitud, manteniendo los signos de puntuación
        Returns:
            str: una nueva cadena con las palabras ordenadas por longitud, separadas por un espacio
    """
    patron = r'[.,¡¿;]*\w+[\w\']*[.,!?;]*'
    palabras = re.findall(patron, cadena)
    return ' '.join(sorted(palabras, key=lambda x: len(re.sub(r'[^\w]', '', x))))

if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    resultado = palabras_ordenadas(frase)
    print(resultado)

# End-of-file (EOF)
