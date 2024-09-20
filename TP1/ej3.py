"""Este programa controla los gasto del subte en un mes."""
def control_gastos(cant: int, valor: int) -> float:
    """Dependiendo la cantidad de viajes que se planean hacer en un mes 
        se llama a la función adecuada.
    
        Args:
            cant (int): Cantidad de viajes en un mes.
            valor (int): Valor máximo del pasaje.
        
        Returns:
            float: el total gastado en viajes.
    """
    if cant < 21:
        total = one_to_twenty(cant, valor)
    elif cant < 31:
        total = calculo_pasaje(cant, valor, 0.8)
    elif cant < 41:
        total = calculo_pasaje(cant, valor, 0.7)
    else:
        total = calculo_pasaje(cant, valor, 0.6)
    return total

def one_to_twenty(cant: int, valor: int) -> float:
    """De 1 a 20 viajes no hay descuentos. El precio por viaje es el valor máximo. """
    return valor * cant

def calculo_pasaje(cant: int, valor: int, percentage: float)-> float:
    """
    Args:
        cant (int): Cantidad de viajes en un mes.
        valor (int): Valor máximo del pasaje.
        percentage (float): La cantidad de descuentos que se aplica 
                            de acuerdo a la cantidad de viajes.
    """
    return cant * (valor * percentage)

def es_valido(dato: int, lim1: int):
    """Una generica para poder establecer limites en los input y verificarlos."""
    return dato > lim1

def main() -> None:
    """Permite al usuario ingresa la cantidad de viajes y el valor máximo."""
    while True:
        try:
            cant = int(input("Ingrese la cantidad de viajes realizados: "))
            valor = int(input("Ingrese el valor de su pasaje: $"))
            break
        except ValueError:
            print("Debe ingresar números enteros.")

    if es_valido(cant, 0) and es_valido(valor, 0):
        total = control_gastos(cant, valor)
        print(f"El total gastado en el mes es de ${total}.")
    else:
        print("Datos no válidos.")


def verificar() -> None:
    """Verifica el comportamiento de la función 'control_gastos'."""
    for i in range(len(test[0])):
        total = control_gastos(test[0][i], test[1][i])
        print(f"El total gastado en el mes es de ${total}.")

test = [[10, 22, 33, 50, 5, 28], [120, 150, 200, 180, 90, 130],]
#0. cant de viajes, 1. valor de pasaje

###Bloque principal
if __name__ == "__main__":
    main()
    print()
    verificar()
#End-of-file (EOF)
