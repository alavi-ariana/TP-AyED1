from typing import List, Dict, Tuple

def pedir_n() -> int:
    """Se le solicita al usuario que ingrese un entero.
    Returns:
        int: un entero mayor a 0.
    """
    while True:
        try:
            n = int(input("Ingrese n: "))
            if n < 0:
                raise ValueError()
            return n
        except ValueError:
            print("Ingresa n positivo xfis.")

def crear_diccionario(n: int) -> Dict:
    """Crea un diccionario por comprensión con n cantidad de elementos.
    Args:
        n: cantidad de elementos a crea, debe ser un entero positivo.
    Returns:
        Dict: con claves hasta n elementos y valores claves al cubo.
    """
    return {x: x**3 for x in range(n)}

def lista_clave(n: int) -> List[int]:
    """Solicita al usuario que ingrese las claves a eliminar en una lista por comprensión.
    Args:
        n: cantidad de elementos a solicitar.
    Returns:
        List[int]: lista de enteros que representan las claves a eliminar.
    """
    while True:
        try:
            return [(int(input("Ingrese las claves a eliminar: "))) for _ in range(n)]
        except ValueError:
            print("Ingrese enteros !!")

def eliminarclaves(diccionario: Dict[int], lista_claves: List[int]) -> Tuple[int, Dict[int]]:
    """Elimina claves de una lista que aparecen en un diccionario y cuánta la cantidad de elem eliminados.
    Args:
        diccionario: diccionario a eliminar las claves.
        lista_claves: claves a eliminar en el diccionario.
    Returns:
        Tuple[int, int]: cantidad de elementos que se eliminaron, 
            diccionario actualizado sin las claves eliminadas.
    """
    cantidad = 0
    for clave in lista_claves:
        if clave in diccionario:
            del diccionario[clave]
            cantidad += 1
    return cantidad, diccionario


def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    while True:
        n = pedir_n()
        diccionario = crear_diccionario(n)
        print(diccionario)
        listaclavicula = lista_clave(n)
        cant, diccionario = eliminarclaves(diccionario, listaclavicula)
        print(f"La cantidad de claves que se borraron fueron {cant}, diccionario actualizado: ")
        print(diccionario)
        break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYE !")

# End-of-file (EOF)
