###Funciones
def es_fecha_valida(day, month, year): #en números enteros
    return months_31days(month, day) or months_30days(month, day) or february(day, year)

def es_bisiesto(year):
    if year % 100 == 0 and year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

def months_31days(month, day):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return day > 0 and day < 32

def months_30days(month, day):
    if month in (4, 6, 9, 11):
        return day > 0 and day < 31
    
def february(day, year):
    if es_bisiesto(year):
        return day > 0 and day < 30
    else:
        return day > 0 and day < 29

def main():
    print("VERIFIQUE SI SU FECHA ES VÁLIDA")
    day = int(input("Ingrese el día: "))
    month = int(input("Ingrese el mes: "))
    year = int(input("Ingrese el año: "))
    if es_fecha_valida(day, month, year):
        print(es_fecha_valida(day, month, year))
        print("Su fecha es válida.")
    else:
        print(es_fecha_valida(day, month, year))
        print("Fecha inválida.")

###Verificación del comportamiento de la función
def verificar():
    while True:
        show_boolean(fechas_validas, 0)
        show_boolean(fechas_invalidas, 0)
        break
    return None

def show_boolean(list, ind):
    for i in range(len(list[ind])):
        print(list[ind][i], list[ind + 1][i], list[ind + 2][i])
        print(es_fecha_valida(list[ind][i], list[ind + 1][i], list[ind + 2][i]))
    return None

fechas_validas = [[29, 28, 31, 30, 1], [2, 2, 12, 6, 1], [2020, 2019, 2023, 2022, 2024],] #día, mes, año cada elemento en el mismo indice es una fecha
fechas_invalidas = [[29, 31, 32, 31, 30], [2, 4, 1, 6, 2], [2019, 2023, 2022, 2023, 2020],]

###Bloque principal
main()
print()
verificar()