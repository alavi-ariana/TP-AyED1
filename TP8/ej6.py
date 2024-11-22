import re

def ingresar_frase() -> str:
    """Solicita al usuario que ingrese un string.
    Returns:
        str: la frase del usuario.
    """
    return input("INGRESE SU FRASE: ")

def no_signos(frase: str) -> str:
    """Elimina los signos de puntiacón de al frase.
    Returns: la frase sin signos de puntiacioón.
    """
    return re.sub(r'[^\w\s]', '', frase)

def ordenar(frase: str) -> str:
    """Ordena los string en una frase por su longitud.
    Args:
        frase: string a ordenar.
    Returns:
        str: la frase ordenada por su longitud.
    """
    frase = set(no_signos(frase).split())
    return ' '.join(sorted(frase, key=len))

def main():
    """Flujo principal que maneja todo el programa.
    Returns: None
    """
    frase = ingresar_frase()
    if not frase:
        print("Debe ingresar una frase >:(")
    else:
        print(f"{ordenar(frase) if ordenar(frase) else 'No se ingresaron palabras.'}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("BYEE !!")

# End-of-file (EOF)
