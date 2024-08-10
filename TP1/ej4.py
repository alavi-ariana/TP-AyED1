###Funciones
def calculo_cash(vuelto):
    cambio = [[5000, 1000, 500, 200, 100, 50, 10], []]
    for billete in cambio[0]:
        cantidad = vuelto // billete
        cambio[1].append(cantidad)
        vuelto %= billete
    return cambio

def dinero_suficiente(total, dinero):
    return dinero >= total

def hay_cash(vuelto):
    return vuelto % 10 == 0

def main():
    total = int(input("Ingrese el total de su compra: $"))
    dinero = int(input("Ingrese con cuánto paga: $"))
    if dinero_suficiente(total, dinero):
        vuelto = dinero - total
        if vuelto > 0 and hay_cash(vuelto):
            cambio = calculo_cash(vuelto)
            print(f"Su vuelto es de ${vuelto}.")
            for i in range(len(cambio[0])):
                print(f"{cambio[1][i]} billetes de ${cambio[0][i]}")
        elif vuelto == 0:
            print("No hay vuelto, usted pagó exacto")
        else:
            print("El vuelto no es posible porque los billetes no alcanzan.")
    else:
        print("Dinero insuficiente.")
    return None
    

###Bloque principal
main()