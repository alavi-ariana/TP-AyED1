###Funciones
def control_gastos(cant, valor):
    if cant < 21:
        total = one_to_twenty(cant, valor)
    elif cant < 31:
        total = calculo_pasaje(cant, valor, 0.8)
    elif cant < 41:
        total = calculo_pasaje(cant, valor, 0.7)
    else:
        total = calculo_pasaje(cant, valor, 0.6)
    return total

def one_to_twenty(cant, valor):
    total = valor * cant
    return total

def calculo_pasaje(cant, valor, porcentage):
    total = cant * (valor * porcentage)
    return total

def es_valido(dato, lim1):
    return dato > lim1

def main():
    cant = int(input("Ingrese la cantidad de viajes realizados: "))
    valor = int(input("Ingrese el valor de su pasaje: $"))
    if es_valido(cant, 0) and es_valido(valor, 0):
        total = control_gastos(cant, valor)
        print(f"El total gastado en el mes es de ${total}.")
    else:
        print("Datos no válidos.")
    return None

###Verificar comportamiento de la función
def verificar():
    for i in range(len(test[0])):
        total = control_gastos(test[0][i], test[1][i])
        print(f"El total gastado en el mes es de ${total}.")
    return None

test = [[10, 22, 33, 50, 5, 28], [120, 150, 200, 180, 90, 130],] #0. cant de viajes, 1. valor de pasaje

###Bloque principal
main()
print()
verificar()