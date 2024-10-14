""" Programa que cuenta cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres  de  la  subcadena  no  necesariamente  deben  estar  en  forma  consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos"""
import re

def contar_subcadena(cadena: str, subcadena: str) -> int:
    """ Cuenta cuántas veces aparece una subcadena en una cadena,
        permitiendo que los caracteres no sean consecutivos pero sí respetando el orden
        Args: 
            - cadena(str): cadena original en la que buscar, no debe estar vacio.
            - subcadena(str): subcadena a buscar en cadena.
        Returns:
            - int: cantidad de coincidencias de subcadena en cadena.
    """
    cadena = cadena.lower()
    subcadena = re.escape(subcadena.lower())

    patron = '.*?'.join(subcadena)
    coincidencias = re.findall(patron, cadena)
    return len(coincidencias)

if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    sub_cadena = input("Ingrese la subcadena a buscar: ")
    if frase and sub_cadena:
        cantidad = contar_subcadena(frase, sub_cadena)
        print(f"La subcadena {sub_cadena} aparece {cantidad} {'vez' if cantidad == 1 else 'veces'}")
    else:
        print("Debe ingresar valores válidos.")


# End-of-file (EOF)
