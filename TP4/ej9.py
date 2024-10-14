""" Programa para recibir una cadena de caracteres y devolverlas ordenadas por su longitud."""
import re

def palabras_ordenadas(cadena: str) -> str:
    """ Ordena las palabras de la cadena según su longitud, manteniendo los signos de puntuación
        Args:
            - cadena(str): cadena a ordenar, no debe estar vacio.
        Returns:
            str: una nueva cadena con las palabras ordenadas por longitud, separadas por un espacio
    """
    patron = r'[.,¡¿;]*\w+[\w\']*[.,!?;]*'
    palabras = re.findall(patron, cadena)
    return ' '.join(sorted(palabras, key=lambda x: len(re.sub(r'[^\w]', '', x))))

if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    if frase:
        resultado = palabras_ordenadas(frase)
        print(resultado)
    else:
        print("Debe ingresar algo.")

# End-of-file (EOF)
