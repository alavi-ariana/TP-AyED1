"""
Este programa busca el mayor y devuelve si es estricto o no, sin utilizar operadores lógicos.
"""
from typing import List

def recibir_numeros(lista: List[int]) -> int:
    """ Determina si el número máximo en la lista es estricto.

        Args: 
            lista (List[int]): Una lista de números enteros. No debe estar vacía.

        Returns:
            int: Si el número máximo es estricto se devuelve el número máximo,
            caso contrario se devuelve -1.
    """
    mayor = max(lista)
    if es_estricto(mayor, lista):
        return mayor
    return -1

def es_estricto(mayor: int, lista: List[int]) -> bool:
    """ Determina si el número máximo aparece solo una vez en la lista.

        Args: 
            mayor (int): El número máximo de la lista.
            lista (List[int]): Una lista con números enteros.

        Returns:
            bool: 'True' si el número máximo aparece solo una vez, 'False' en caso contrario.
    """
    count = lista.count(mayor)
    return count == 1

def main() -> None:
    """ El usuario ingresa números hasta que pare y 
        se le comunica si el número más grande es estricto.
    """
    lista: List[int] = []
    while True:
        print(lista)
        try:
            num_op = int(input("Ingrese el número (-1 para salir): "))
        except ValueError:
            print("Sólo debe ingresar números enteros.")
        if num_op == -1:
            break

        lista.append(num_op)

    if len(lista) == 0:
        print("Lista vacia.")
    else:
        resultado = recibir_numeros(lista)
        if resultado == -1:
            print("No existe un mayor estricto.")
        else:
            print(f"El número mayor estricto es {resultado}.")



if __name__ == "__main__":
    main()
#End-of-file (EOF)
