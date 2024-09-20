"""Programa para el manejo de cosecha de naranjas y su transporte."""
import random as rn
rn.seed(100)

MAX_PESO_CAJON = 300
MIN_PESO_CAJON = 200
MAX_CAMION = 500
MIN_CAPACIDAD_CAMION = MAX_CAMION * 0.8

def clasificar(naranjas_op: int) -> tuple:
    """ Claficia las naranjas cosechadas en cajones y naranjas para jugo, y 
        calcula el peso total.
        Args:
            - naranjas_op: es un entero positivo.
        Returns: 
            - tuple: 
                - boxes: es la cantidad de cajones llenas (con un máximo de 100 naranjas)
                - juice: cantidad de naranjas no aptas para el cajón y usadas para el jugo
                - total_weight / 1000: el peso total de las naranjas en cajones en kg
                - oranges_left: la cant de naranjas sobrantes que no alcanzaron para llenar un cajón
    """
    cajon = 100
    naranja_pesos = weight(naranjas_op)
    boxes, juice, total_weight, orangesperbox = 0, 0, 0, 0
    for valor in naranja_pesos:
        if valor >= MIN_PESO_CAJON and valor <= MAX_PESO_CAJON:
            cajon -= 1
            total_weight += valor
            orangesperbox += 1
            if cajon == 0:
                boxes += 1
                cajon = 100
                orangesperbox = 0
        else:
            juice += 1

    oranges_left = orangesperbox

    return boxes, juice, total_weight / 1000, oranges_left

def camion(total_weight: int) -> int:
    """ Calcula la cantidad de camiones necesarios para transportar la cosecha
        Args:
            - total_weight: es un entero que representa el peso total de las naranjas
        Returns:
            - Cantidad de camiones necesarios para transporta la cosecha.
    """
    camiones = 0
    while total_weight > 0:
        if total_weight >= MAX_CAMION:
            camiones += 1
            total_weight -= MAX_CAMION
        elif total_weight >= MIN_CAPACIDAD_CAMION:
            camiones += 1
            total_weight = 0
        else:
            break
    return camiones


def weight(unidad: int) -> list[int]:
    """ Genera una lista de pesos aleatorios para las naranjas.
        Args:
            - unidad: es un entero que representa la cantidad de naranjas a generar
        Returns:
            - Retorna una lista de enteros con pesos aleatorios entre 150g y 350g
    """
    return list(rn.randint(150, 350) for _ in range(unidad))

if __name__ == "__main__":
    while True:
        try:
            orange_op = int(input("Ingrese la cantidad de naranjas cosechadas: "))
            if orange_op > 0:
                break
            print("Sólo valores mayor a 0.")
        except ValueError:
            print("Debe ingresar números enteros positivos.")

    cajones, jugo, peso_total, sobra_naranjas = clasificar(orange_op)

    print(f"Cajones llenados: {cajones} y el peso total {peso_total}kg")
    print(f"Naranjas para jugo: {jugo}")
    print(f"Naranjas sobrantes para el siguiente reparto: {sobra_naranjas}")
    cant_camiones = camion(peso_total)
    print(f"Cantidad de camiones necesarios para transportar la cosecha: {cant_camiones}")



# End-of-file (EOF)
