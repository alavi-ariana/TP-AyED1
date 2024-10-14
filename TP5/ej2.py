"""Programa que  reciba como  parámetros dos  cadenas  de  caracteres  con-
teniendo  números  reales,  sume  ambos  valores  y  devuelva  el  resultado  como  un 
número  real. Devolver -1  si alguna de las cadenas no contiene un número  válido, 
utilizando manejo de excepciones para detectar el error."""
import re
from typing import List
from functools import reduce

def suma(valores: str) -> float:
    """Suma los dos números que se encuentren en valores.
    Args:
        - valores: cadenas con números.
    Returns:
        - float: siempre retorna un entero, sea el resultado de la suma o -1 si no se pudo realizar.
    """
    try:
        numeros = sacar_nums(valores)
        print(numeros)
        if len(numeros) > 1:
            return reduce(lambda x, y: x + y, numeros)
        raise ValueError
    except ValueError:
        return -1
    except TypeError:
        return -1

def sacar_nums(cadena: str) -> List[float]:
    """Extrae de una cadena los números que encuentre.
    Args:
        - cadena(str): cadena de la cual extraer los números.
    Returns:
        - List[float]: una lista con todos los números extraidos de aquella cadena.
    """
    numeros = re.findall(r'\d+\.\d+|\d+', cadena)
    return [float(numero) for numero in numeros]

def main() -> None:
    """Ejecuta todo el código.
    Args:
        - None
    Returns:
        - None
    """
    while True:
        try:
            valores = input("Ingrese los números separados por comas: ")
            break
        except ValueError:
            print("Ingrese valores válidos.")

    numeros_sumados = " + ".join(map(str, sacar_nums(valores)))
    resultado = suma(valores)
    if resultado == -1:
        print("No se pudo realizar la suma.")
    else:

        print(f"La suma de los números {numeros_sumados} = {resultado}")

if __name__ == "__main__":
    main()

# End-of-file (EOF)
