from typing import Dict

def ingresar_n() -> int:
    """Solicita al usuario un número entero.
    Reeturns:
        int: el número entero del usuario.
    """
    try:
        return int(input("Ingrese un entero: "))
    except ValueError:
        print("Te dije que ingreses un entero.")

def tabla(n: int) -> Dict:
    """Genera la tabla de multiplicar de N, del 1 al 12.
    Args:
        n: número a multiplicar.
    Returns:
        Dict: diccionario por comprensión con las multiplicaciones.
    """
    return {x: n*x for x in range(1, 13)}

def main() -> None:
    """Flujo principal que maneja todo el programa.
    Returns: None
    """
    n = ingresar_n()
    if n:
        tabla_n = tabla(n)
        for i in range(1, 13):
            print(f"{n} x {i} = {tabla_n[i]}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE !!")
