""" Programa para crear matriz sin intervención humana"""

def matriz_a(n: int) -> list[list[int]]:
    """Genera una matriz en la diagonal principal con número crecientes + 2"""
    return [[2 * i + 1 if i == j else 0 for j in range(n)] for i in range(n)]


def matriz_b(n: int) -> list[list[int]]:
    """Genera una matriz con la diagonal secundaria con la división por 3 de 27"""
    return [[27 // (3 ** i) if j == n-1-i else 0 for j in range(n)] for i in range(n) ]

def matriz_c(n: int) -> list[list[int]]:
    """Genera una matriz a partir de la diagonal principal con números decrecientes"""
    return [[n - i if j <= i else 0 for j in range(n)]for i in range(n)]


def matriz_d(n: int) -> list[list[int]]:
    """Genera una matriz todas las posiciones con el 8 dividido 2"""
    return [[8 // (2 ** i) for _ in range(n)]for i in range(n)]

def matriz_e(n: int) -> list[list[int]]:
    """Genera una matriz con valores crecientes en posiciones alternadas"""
    valor = 0
    return [[(valor := valor + 1) if (i + j) % 2 == 1 else 0 for j in range(n)]for i in range(n)]

def matriz_f(n: int) -> list[list[int]]:
    """Genera una matriz a partir de la diagonal secundaria con números crecientes"""
    valor = 0
    return [[(valor := valor + 1) if j >= n-1-i else 0 for j in range(n)]for i in range(n)]

def show_matriz(matriz: list[list[int]]):
    """Se muestra en la terminal la matriz de forma cuadrada"""
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()

if __name__ == "__main__":
    try:
        n = int(input("Ingrese el tamaño N de la matriz: "))

        print("MATRIZ A")
        show_matriz(matriz_a(n))

        print("MATRIZ B")
        show_matriz(matriz_b(n))

        print("MATRIZ C")
        show_matriz(matriz_c(n))

        print("MATRIZ D")
        show_matriz(matriz_d(n))

        print("MATRIZ E")
        show_matriz(matriz_e(n))

        print("MATRIZ F")
        show_matriz(matriz_f(n))
    except ValueError:
        print("Debe ingresar un entero.")

# End-of-file (EOF)
