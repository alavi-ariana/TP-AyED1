"""Programa para indicar cuánto es el vuelto a un cajero con la minima cantidad de billetes."""

def calculo_cash(vuelto: int) -> list[list[int]]:
    """Se hace el calculo de los billetes a devolver.

        Returns:
            list[list[int]]: Se devuelve la lista con la cantidad de 
                            billetes usados por cada billete, por lo cual se devuelve el cambio.
    """
    cambio: list[list[int]] = [[5000, 1000, 500, 200, 100, 50, 10], []]
    for billete in cambio[0]:
        cantidad = vuelto // billete
        cambio[1].append(cantidad)
        vuelto %= billete
    return cambio

def dinero_suficiente(total: int, dinero: int) -> bool:
    """Corrobora que el dinero entregado sea suficiente para pagar la compra.
    
        Args:
            total (int): El total de la compra.
            dinero (int): El dinero recibido por el cajero.
        
        Returns:
            bool: 'False' si el dinero es menor al total por lo tanto no se llega a pagar la compra, 
                caso contrario 'True'.
    """
    return dinero >= total

def hay_cash(vuelto: int) -> bool:
    """ Se revisa si el vuelto es divisor de 10 para poder hacer la entrega del vuelto 
        con los billetes que se tienen en la caja.

        Returns:
            bool: 'False' si no será posible hacer la devolución en billetes (no divisor de 10), 
                caso contrario 'True'.
    """
    return vuelto % 10 == 0

def main() -> None:
    """Permite al usuario ingresar los valores de total y dinero."""
    while True:
        try:
            total = int(input("Ingrese el total de su compra: $"))
            dinero = int(input("Ingrese con cuánto paga: $"))
            break
        except ValueError:
            print("Debe ingresar números enteros.")
            continue

    if dinero_suficiente(total, dinero):
        vuelto = dinero - total
        if vuelto > 0 and hay_cash(vuelto):
            cambio = calculo_cash(vuelto)
            print(f"\nSu vuelto es de ${vuelto}.")
            for i in range(len(cambio[0])):
                print(f"{cambio[1][i]} billetes de ${cambio[0][i]}")
        elif vuelto == 0:
            print("No hay vuelto, usted pagó exacto")
        else:
            print("El vuelto no es posible porque los billetes no alcanzan.")
    else:
        print("Dinero insuficiente.")


main()
#End-of-file (EOF)
