from math import sqrt

def raiz_cuadrada(num: int) -> float:
    """Recibe un número y devuelve su raíz cuadrada.
    Args:
        int: debe ser un número positivo y no vacio.
    Returns:
        float: la raíz del número.
    """
    try:
        print(f"La raiz cuadrada de {num} es {sqrt(num)}")
    except ValueError:
        print("Debe ingresar solo positivos.")

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    while True:
        try:
            num_op = int(input("Ingrese el número a sacar la raíz cuadrada: "))
            break
        except ValueError:
            print("Debe ingresar valores válidos.")
    raiz_cuadrada(num_op)

if __name__ == "__main__":
    main()
# End-of-file (EOF)
