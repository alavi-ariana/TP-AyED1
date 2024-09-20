""" Programa para crear una lista con número al cuadraro entre 1 y n (incluido).
    Luego muestra los últimos 10 elementos de la lista."""
def lista_cuadrados(n: int) -> list[int]:
    """Genera una lista con elementos elevado al cuadrado entre 1 y n."""
    return [i ** 2 for i in range(1, n + 1)]

if __name__ == "__main__":
    while True:
        try:
            op = int(input("Ingrese un número: "))
            if op > 0:
                break
        except ValueError:
            print("Solo debe ingresar valores enteros positivos.")
    listorta = lista_cuadrados(op)
    print(listorta)
    for elem in listorta[-10:]:
        print(elem)

# End-of-file (EOF)
