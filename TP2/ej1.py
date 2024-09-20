"""Diferentes funciones"""
import random as rn
from functools import reduce
rn.seed(10)

def producto() -> int:
    """Calcula y devuelve el producto de todos los elementos de la lista.
    """
    return reduce(lambda x, y: x * y, lista_azar)

def eliminar_valor(valor: int) -> list[int]:
    """Elimina todas las apariciones de un valor en la lista.
        Args:
            int: el valor para borrar de la lista.
        returns:
            list[int]: se devuelve la lista original modificada."""
    lista_azar [:] = [elemento for elemento in lista_azar if elemento != valor]
    return lista_azar

def capicua(lista: list[int]) -> bool:
    """ Verifica si una lista es capicua.
        Args:
            - Lista: Se espera una lista con elementos.
        returns:
            bool: True sí es, caso contrario False.
    """
    for i in range(len(lista) // 2):
        if lista[i] != lista[len(lista) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    cant_elem = rn.randint(10, 99)
    lista_azar = [rn.randint(1000, 9999) for _ in range(cant_elem)]
    print(lista_azar)
    print(f"El producto de todos los elementos es: {producto()}")
    while True:
        try:
            valor_op = int(input("Ingrese el valor a eliminar: "))
            break
        except ValueError:
            print("Solo enteros.")
    if valor_op in lista_azar:
        print(eliminar_valor(valor_op))
    else:
        print("Elemento no pertenece a la lista.")

    print("AVERIGUE SI SU LISTA ES CAPICUA")
    capi = []
    while True:
        try:
            elem_op = int(input("Ingrese elementos en la lista (-1 para salir): "))
            if elem_op == -1:
                break
            capi.append(elem_op)
        except ValueError:
            print("Solo valores enteros.")
    print(capi)
    if not capi:
        print("Lista vacia.")
    else:
        print(f"El valor de capicua es {capicua(capi)}")

# End-of-file (EOF)
