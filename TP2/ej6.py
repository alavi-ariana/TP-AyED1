"""Programa para normalizar una lista de números"""
def normalizar(lista: list[int]) -> list:
    """ Normaliza una lista.
        Returns:
            - list: retorna una lista con todos los elementos normalizados.
    """
    suma_total = sum(lista)
    if suma_total == 0:
        return []
    return [elem / suma_total for elem in lista]


if __name__ == "__main__":
    listorta = []
    while True:
        try:
            op = int(input("Ingrese los números para la lista (-1 para salir): "))
            if op == -1:
                break
            listorta.append(op)
        except ValueError:
            print("Solo valores enteros.")
    
    if not listorta:
        print("Lista vacia.")
    else:
        print(f"Lista original: {listorta}")
        listorta = normalizar(listorta)
        print(f"Lista normalizada: {listorta}")

# End-of-file (EOF)
