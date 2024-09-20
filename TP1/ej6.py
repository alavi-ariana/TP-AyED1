"""Programa que concatena dos números enteros positivos."""
def calculo(a: int, b: int) -> int:
    """ Se toman dos enteros positivos 'a' y 'b' y se retorna un entero que
        representa la concatenación de 'a' y 'b'.
    """
    contador = 0
    aux = b
    while aux > 0:
        aux //= 10
        contador += 1
    return a * (10 ** contador) + b


def main() -> None:
    """ Se le solicita al usuario ingresar dos números enteros positivos,
        para luego mostrar la concatenación de los dos números.
    """
    while True:
        try:
            a = int(input("Ingresar primer número: "))
            b = int(input("Ingresar segundo número: "))
            if a > 0 and b > 0:
                break
            print("Se necesitan valores enteros positivos.")
        except ValueError:
            print("Ingrese números enteros.")
    resultado = calculo(a, b)
    print(f"El número concatenado es {resultado}")

if __name__ == "__main__":
    main()
#End-of-file (EOF)
