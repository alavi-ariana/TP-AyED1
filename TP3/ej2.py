""" Programa para crear matriz sin intervención humana"""

def matriz_a(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    for i in range(N):
        matriz[i][i] = 2 * i + 1
    return matriz


def matriz_b(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    valor = 27
    for i in range(N):
        matriz[i][N - 1 - i] = valor
        valor //= 3
    return matriz

def matriz_c(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            matriz[i][j] = N - i
    return matriz


def matriz_d(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    valor = 8
    for i in range(N):
        matriz[i] = [valor] * N
        valor //= 2
    return matriz

def matriz_e(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    valor = 1
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 1:
                matriz[i][j] = valor
                valor += 1
    return matriz


def show_matriz(matriz: list[list[int]]):
    """Se muestra en la terminal la matriz de forma cuadrada"""
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()

if __name__ == "__main__":
    try:
        N = int(input("Ingrese el tamaño N de la matriz: "))

        print("MATRIZ A")
        show_matriz(matriz_a(N))

        print("MATRIZ B")
        show_matriz(matriz_b(N))

        print("MATRIZ C")
        show_matriz(matriz_c(N))

        print("MATRIZ D")
        show_matriz(matriz_d(N))

        print("MATRIZ E")
        show_matriz(matriz_e(N))
    except ValueError:
        print("Debe ingresar un entero.")

# End-of-file (EOF)
