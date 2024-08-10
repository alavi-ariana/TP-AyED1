###Funciones

def recibir_numeros(num1,  num2, num3):
    mayor = max(num1, num2, num3)
    if es_estricto(mayor, num1, num2, num3):
        return mayor
    return -1

def verificar_maximo(mayor, num1, num2, num3):
    count = 0
    if mayor == num1:
        count += 1
    if mayor == num2:
        count += 1
    if mayor == num3:
        count += 1
    return count

def es_estricto(mayor, num1, num2, num3):
    count = verificar_maximo(mayor, num1, num2, num3)
    return count == 1

def app():
    num1 = int(input("Ingrese el número: "))
    num2 = int(input("Ingrese el número: "))
    num3 = int(input("Ingrese el número: "))
    resultado = recibir_numeros(num1, num2, num3)
    if resultado == -1:
        print("No existe un mayor estricto.")
    else:
        print(f"El número mayor estricto es {resultado}.")
    return None

###Bloque principal
app()


