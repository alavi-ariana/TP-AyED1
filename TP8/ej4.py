from typing import Tuple

def domino_encaja(fichas1: Tuple[int, int], fichas2: Tuple[int, int]) -> bool:
    """Corrobora que las fichas del domino encajan, utilizando el '&' operador
        (la intersección de conjuntos).
        Args:
            - 'ficha1' y 'ficha2': tuplas con enteros a corroborar si encajan.
        Returns:
            - bool: True si las fichas encajan caso contrario False.
        """
    return bool(set(fichas1) & set(fichas2))

def solicitar_domino() -> Tuple[int, int]:
    """Le solicita al usuario las fichas del domino.
    Returns:
        - Tuple[int, int]: las fichas con los dos enteros.
    """
    while True:
        fichas1 = input("Ingrese el primer conjunto de fichas separados por comas (x,y): ")
        fichas2 = input("Ingrese el segundo conjunto de fichas separados por comas (x,y): ")
        try:
            fichas1 = tuple(map(int, fichas1.split(",")))
            fichas2 = tuple(map(int, fichas2.split(",")))
            if len(fichas1) == 2 and len(fichas2) == 2:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar dos valores enteros.")
    return fichas1, fichas2

def validar_ficha(ficha: Tuple[int, int]) -> bool:
    """Verifica que las fichas esten entre los rangos del domino válidos.
    Args:
        - Tuple[int, int]: los enteros de la tupla serán los que se corroboran si son válidos.
    Returns:
        - bool: True si son válidos, caso contrario False.
    """
    num1, num2 = ficha
    return 0 <= num1 < 7 and 0 <= num2 < 7

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    fichas1, fichas2 = solicitar_domino()
    if validar_ficha(fichas1) and validar_ficha(fichas2):
        if domino_encaja(fichas1, fichas2):
            print("Las fichas encajan !!")
        else:
            print("Las fichas no encajan :(")
    else:
        print("Debe ingresar valores válidos entre 0-6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE!!")

# End-of-file (EOF)
