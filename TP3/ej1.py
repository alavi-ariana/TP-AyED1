"""Programa con muchas funciones e imprime la matriz cada en cada llamado de función"""
#def a(N):
#    return [[for i in range(N)] for j in range(N)]

def a(n: int) -> list[list[int]]:
    """Carga una matriz de tamaño nxn con valores ingresados por el usuario."""
    return [[int(input(f"Ingrese el elemento en la posición {j + 1} de la lista {i + 1}")) for j in range(n)] for i in range(n)]

def b() -> list[list[int]]:
    """ Ordena cada fila de la matriz en forma ascendente."""
    for fila in matriz:
        fila.sort()
    return matriz

def c(num: int, num2: int) -> None:
    """ Intercambia dos filas de la matriz en la posición de la otra."""
    matriz[num], matriz[num2] = matriz[num2], matriz[num]

def d(num: int, num2: int) -> None:
    """ Intercambia dos columnas de la matriz en la posición de la otra."""
    for fila in matriz:
        fila[num], fila[num2] = fila[num2], fila[num]

def e() -> None:
    """Transpone la matriz sobre sí misma."""
    longitud = len(matriz)
    for i in range(longitud):
        for j in range(1 + 1, longitud):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def f(fila_op: int) -> float:
    """ Calcula el promedio de los elementos de una fila especifica"""
    total = 0
    suma = 0
    for fila in matriz:
        if fila == fila_op:
            for elem in fila:
                total += 1
                suma += elem
    promedio = suma / total
    return promedio

def g(colum_op: int) -> float:
    """ Calcula el porcentaje de elementos impares en una columna dada"""
    total = sum(1 for fila in matriz if fila[colum_op] % 2 != 0)
    suma = len(matriz)
    return (total / suma) * 100

def h() -> bool:
    """ Determina si la matriz es simétrica respecto a su diagonal principal"""
    longitud = len(matriz)
    for i in range(longitud):
        for j in range(longitud):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def i() -> bool:
    """ Determina si la matriz es simétrica respecto a su diagonal secundaria. """
    longitud = len(matriz)
    for i in range(longitud):
        for j in range (longitud):
            if matriz[i][j] != matriz[longitud - 1 - j][longitud - 1 - i]:
                return False
    return True

def mostrar_matriz() -> None:
    """ Muestra la matriz"""
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    N =int(input("Ingrese el valor de N para la matriz NxN: "))

    matriz = a(N)
    mostrar_matriz()

    b()
    mostrar_matriz()

    num = int(input("Ingrese el número de la fila a intercambiar: "))
    num2 = int(input("Ingrese el número de la fila con la que intercambiarla: "))
    c(num, num2)
    mostrar_matriz()

    nnumi = int(input("Ingrese el número de la columna a intercambiar: "))
    nnumi2 = int(input("Ingrese la otra columna a intercambiar: "))
    d(nnumi, nnumi2)
    mostrar_matriz()

    e()
    mostrar_matriz()

    fila_op = int(input("Ingrese el número de fila para calcular el promedio: "))
    promedio = f(fila_op)
    print(f"El promedio es de {promedio}")
    mostrar_matriz()

    colum_op = int(input("Ingrese la columna para calcular el porcentaje de impares: "))
    porcentaje = g(colum_op)
    print(f"El porcenta de elementos impares en la columan {colum_op} es: {porcentaje:.2f}%")

    simetrica_principal = h()
    print(f"El valor de simetria de la matriz es {simetrica_principal}")

    simetrica_secundaria = i()
    print(f"El valor de simetría secundaria de la matriz es {simetrica_secundaria}")

# End-of-file (EOF)
