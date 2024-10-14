"""Convertido a número romanoentre 0 y 3999"""
def romano(entero: int) -> str:
    """ Convierte un número entero en su representación en números romanos
        Args:
            - entero (int): número a convertir, debe ser mayor a 0 y menor a 3999.
        Returns:
            - str: la conversión a número romano del entero.
    """
    num_rom = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    resultado = ""
    for valor, simbolo in num_rom:
        while entero >= valor:
            resultado += simbolo
            entero -= valor
    return resultado

if __name__ == "__main__":
    while True:
        try:
            num_op = int(input("Ingrese el número a pasar a romano: "))
            if num_op < 1 or num_op > 3999:
                print("Ingrese un número entre 1 y 3999.")
            else:
                break
        except ValueError:
            print("Solo enteros.")
    romano_result = romano(num_op)
    print(f"El resultado del número {num_op} en romano es {romano_result}")

# End-of-file (EOF)
