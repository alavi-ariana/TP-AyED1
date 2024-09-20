""" Eliminar de una lista aquellos valores que se encuentren en una segunda lista.
    Se debe modificar la lista original."""
import random as rn

def generar_lista(n: int) -> list[int]:
    """Genera una lista con n cantidad de elementos."""
    return [rn.randint(1, 200) for _ in range(n)]

def borrar_num() -> list[int]:
    """Se borra de la lista original elementos de una lista secundaria"""
    return [elem for elem in listorta if elem not in eliminar]

if __name__ == "__main__":
    while True:
        try:
            op = int(input("Ingrese la cantidad de elementos en la lista: "))
            if op > 0:
                break
        except ValueError:
            print("Solo valores enteros positivos.")
    listorta = generar_lista(op)
    print(f"Lista original: {listorta}")
    eliminar = []
    while True:
        try:
            items = int(input("Ingrese los valores a eliminar(-1 para salir): "))
            if items == -1:
                break
            eliminar.append(items)
        except ValueError:
            print("Solo valores enteros positivos.")

    print(f"Lista original: {listorta}")
    listorta = borrar_num()
    print(f"Lista de elementos a borrar: {eliminar}")
    print(f"Lista modificada: {listorta}")
