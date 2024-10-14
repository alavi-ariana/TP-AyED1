""" Lista por comprensión entre A y B con los múltiplos de 7 que no sean
    múltiplos de 5."""
if __name__ == "__main__":
    a = []
    b = []
    while True:
        try:
            min_a = int(input("Ingrese el rango a: "))
            max_b = int(input("Ingrese el rango b: "))
            break
        except ValueError:
            print("Solo enteros.")

    lista = [num for num in range(min_a, max_b) if num % 7 == 0 and num % 5 != 0]
    print(lista)

# End-of-file (EOF)
