import random as rn
from typing import Set

def generar_conjunto(n: int) -> Set[int]:
    """Genera un conjunto con n cantidad de intentos.
    Args:
        n: cantidad de intentos a hacer para rellenar el conjunto.
    Returns:
        Set: conjunto con elementos enteros.
    """
    conjunto = set()
    for _ in range(n):
        conjunto.add(rn.randint(0, 9))
    return conjunto

def pedir_n() -> int:
    """Se le solicita al usuario la cantidad de veces que se debe crear un número para el conjunto.
    Returns:
        int: un entero que representa la cantidad de elementos.
    """
    try:
        n = int(input("Ingrese la cantidad de elementos en el conjunto: "))
        if n < 0:
            raise ValueError()
        return n
    except ValueError:
        print("Debe ingresar un entero positivo.")

def valores_op() -> int:
    """Se le solicita al usuario los número a eliminar del conjunto.
    Returns:
        int: número del usuario.
    """
    try:
        return int(input("Ingrese número a eliminar: "))
    except ValueError:
        print("Debe ingresar un entero.")

def eliminar(op, conjunto) -> Set[int]:
    """Elimina del conjunto el número dado por el usuario.
    Args:
        op: entero a borrar.
        conjunto: conjunto de dónde borrar el entero.
    Returns:
        set: el conjunto actualizado.
    """
    try:
        return conjunto.remove(op)
    except KeyError:
        print("El numero no se encuentra en el conjunto !")

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    n = pedir_n()
    if n:
        conjunto = generar_conjunto(n)
        while True:
            if not conjunto:
                print("Se terminaron los números :(")
                break
            print(conjunto)
            eliminar_op = valores_op()
            if eliminar_op == -1:
                break
            eliminar(eliminar_op, conjunto)
    else:
        print("No me mandaste un entero...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE !!!")

# End-of-file (EOF)
