""" Programa"""
import random as rn

def generar_matriz_aleatoria(N: int) -> list[list[int]]:
    """Genera una matriz de tamaño NxN con números aleatorios únicos entre 0 y N**2"""
    numeros_posibles = list(range(N**2))

    matriz = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            num = rn.choice(numeros_posibles)
            matriz[i][j] = num
            numeros_posibles.remove(num)
    return matriz

def show_matriz(matriz: list[list[int]]) -> None:
    """Se muestra en la terminal la matriz de forma cuadrada"""
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()

if __name__ == "__main__":
    try:
        while True:
            N = int(input("Ingrese el tamaño N de la matriz: "))
            if N > 0:
                break
    except ValueError:
        print("Solo enteros.")
    
    matriorca = generar_matriz_aleatoria(N)
    show_matriz(matriorca)

# End-of-file (EOF)
