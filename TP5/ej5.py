from math import sqrt

def raiz_cuadrada(num: int) -> int:
    try:
        print(f"La raiz cuadrada de {num} es {sqrt(num)}")
    except ValueError:
        print("Debe ingresar solo positivos.")

if __name__ == "__main__":
    while True:
        try:
            num_op = int(input("Ingrese el número a sacar la raíz cuadrada: "))
            break
        except ValueError:
            print("Debe ingresar valores válidos.")
    raiz_cuadrada(num_op)

# End-of-file (EOF)
