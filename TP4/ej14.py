""" Programa para leer correos electronicos y verificar si son válidos o no,
    también muestra los dominios alfabeticamente"""
import re

def correo_valido(correo: str) -> bool:
    """Verifica si un mail es válido según:
        - el nombre de usuario es alfanumérico
        - contiene un solo carácter @
        - el dominio tiene al menos un carácter
        - el dominio termina en .com o .com.ar
        Args:
            - correo(str): correo a verificar.
        Returns:
            bool: True si el correo es válido, caso contrario False.
    """
    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$'
    return bool(re.match(patron, correo))

def sacar_dominio(correo: str) -> str:
    """ Extacción y retorno del dominio del mail.
        Args:
            - correo(str): correo de donde extraer el dominio.
        Returns:
            - str: dominio extraido.
    """
    return correo.split("@")[1]

if __name__ == "__main__":
    dominios: set = set()

    while True:
        mail = input("Ingrese un mail (o presione enter para salir): ").strip().lower()

        if mail == "":
            break

        if correo_valido(mail):
            print(f"{mail} es un correo válido")
            dominios.add(sacar_dominio(mail))
        else:
            print(f"{mail} es un correo no válido")

    print("DOMINIOS ORDENADOS ALFABETICAMENTE")
    for domino in sorted(dominios):
        print(domino)

# End-of-file (EOF)
