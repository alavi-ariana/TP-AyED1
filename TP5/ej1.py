"""Programa que valida un número del usuario con el manejo de excepciones."""

def pedir_num() -> int:
    """Le pide al usuario un número que debe ser entero y mayor a 0.
    Args:
        - None
    Returns:
        - int: el número del usuario solo si es válido (entero mayor a 0).
    """
    try:
        num_op = int(input("Ingrese un número: "))
        if num_op <= 0:
            raise ValueError("Debe ingresar un número mayor a 0.")
        return num_op
    except ValueError as e:
        print(f"Error: {e}")

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    while True:
        op = pedir_num()
        if op:
            break
    print(f"Su número es {op}")

if __name__ == "__main__":
    main()

# End-of-file (EOF)
