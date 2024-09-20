"""Programa para generar lista aleatorio entre 1 al 100 con la cantidad de elementos N.
    Devuelve True si la lista tiene algun elemento repetido. Devuelve una lista con
    elementos únicos de la lista original."""
import random as rn

def lista_aleatorio(n: int) -> list[int]:
    """Genera una lista aleatoria de n cantidad de elementos"""
    return [rn.randint(1, 100) for _ in range(n)]

def repetido(lista: list[int]) -> bool:
    """ Ve si la lista contiene algún elemento repetido."""
    return any(lista.count(x) > 1 for x in lista)

def lista_unica(lista: list[int]) -> list[int]:
    """Genera una lista con los elementos que aparecen solo una vez en la lista original."""
    return list(filter(lambda x: lista.count(x) == 1, lista))

if __name__ == "__main__":
    while True:
        try:
            op = int(input("Ingrese la cantidad de números en la lista: "))
            if op > 0:
                break
        except ValueError:
            print("Solo enteros positivos.")
    listorta = lista_aleatorio(op)
    print(listorta)
    print(f"La repetición de elementos en la lista es {repetido(listorta)}")
    listorta_unica = lista_unica(listorta)
    if not listorta_unica:
        print("No hay elementos únicos.")
    else:
        print(f"Lista con solo los elementos únicos: {lista_unica(listorta)}")

# End-of-file (EOF)
