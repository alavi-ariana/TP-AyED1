""" Programa para recibir una frase y devolver cadena de palabras
    con N longitud de la frase"""
import re

def filtrar_palabras(cadena: str, n: int) -> str:
    """ Filtra las palabras de una cadena que tienen n o más caracteres
        Args:
            - cadena(str): la frase original, no debe ser vacio.
            - n (int): el número mínimo de caracteres que deben tener las palabras para el resultado
        Returns:
            - str: una cadena con las palabras que tienen n o más caracteres, separadas por espacios
    """
    patron = r'\b\w{' + str(n) + r',}\b'
    palabras_filtradas = re.findall(patron, cadena)
    return ' '.join(palabras_filtradas)

def filtrar_x_ciclo(cadena: str, n: int) -> str:
    """ Filtra las palabras de una cadena que tienen n o más caracteres haciendo uso de ciclos
            Args:
            - cadena(str): la frase original, no debe ser vacio.
            - n (int): el número mínimo de caracteres que deben tener las palabras para el resultado
        Returns:
            - str: una cadena con las palabras que tienen n o más caracteres, separadas por espacios
    """
    resultado = []
    palabras = cadena.split()
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return ' '.join(resultado)

def filtrar_listra_comprension(cadena: str, n: int) -> str:
    """ Filtra las palabras de una cadena que tienen n o más caracteres haciendo uso de listas
        por comprensión
            Args:
            - cadena(str): la frase original, no debe ser vacio.
            - n (int): el número mínimo de caracteres que deben tener las palabras para el resultado
        Returns:
            - str: una cadena con las palabras que tienen n o más caracteres, separadas por espacios
    """
    return ' '.join([palabra for palabra in cadena.split() if len(palabra) >= n])

def filtrar_filter(cadena: str, n: int) -> str:
    """ Filtra las palabras de una cadena que tienen n o más caracteres haciendo uso de filter()
            Args:
            - cadena(str): la frase original, no debe ser vacio.
            - n (int): el número mínimo de caracteres que deben tener las palabras para el resultado
        Returns:
            - str: una cadena con las palabras que tienen n o más caracteres, separadas por espacios
    """
    return ' '.join(filter(lambda palabra: len(palabra) >= n, cadena.split()))


if __name__ == "__main__":
    while True:
        try:
            frase = input("Ingrese una frase: ")
            if frase:
                n_op = int(input("Ingrese el número de longitud de las palabras: "))
                break
        except ValueError:
            print("Debe ingresar valores válidos.")

    resultado_patron = filtrar_palabras(frase, n_op)
    resultado_ciclo = filtrar_x_ciclo(frase, n_op)
    resultado_lista = filtrar_listra_comprension(frase, n_op)
    resultado_filter = filtrar_filter(frase, n_op)

    if not resultado_patron:
        print("No hay coincidencias.")
    else:
        print(f"Palabras filtradas mediante RE: {resultado_patron}")
        print(f"Palabras filtradas mediante ciclos: {resultado_ciclo}")
        print(f"Palabras filtradas mediante listas por comprensión: {resultado_lista}")
        print(f"Palabras filtradas mediante el uso de filter(): {resultado_filter}")

# End-of-file (EOF)
