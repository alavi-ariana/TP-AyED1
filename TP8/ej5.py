from typing import Tuple

def pedir_vectores() -> Tuple[int,int]:
    """Solicita al usuario vectores, si son válidos los devuelve.
    Returns:
        Tuple[int, int]: el vector con sus componentes (x,y).
    """
    while True:
        vector = input("Ingrese x,y separados por ',' (x,y): ")
        try:
            x, y = tuple(map(int, vector.split(',')))
            break
        except ValueError:
            print("Debe ingresar valores válidos.")
    return x, y

def ortogonales(vector1, vector2) -> bool:
    """Verifica si los dos vectores son ortogonales, cuando son perpendiculares entre sí.
    Args:
        vector1, vector2: dos tuplas a comparar entre sí para ver si son ortogonales, contienen enteros.
    Returns:
        bool: True si son ortogonales, caso contrario False.
    """
    x1, y1 = vector1
    x2, y2 = vector2
    resultado = x1 * x2 + y1 * y2
    if resultado == 0:
        return True
    return False

def main() -> None:
    """Flujo principal que maneja todo el programa.
    Returns: None
    """
    print("PRIMER VECTOR")
    vector1 = pedir_vectores()
    print("SEGUNDO VECTOR")
    vector2 = pedir_vectores()
    if ortogonales(vector1, vector2):
        print("SON ORTOGONALES !!")
    else:
        print("no son ortogonales :(")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE !!")
# End-of-file (EOF)
