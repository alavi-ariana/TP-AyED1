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
        print("Su fecha es válida.")
    else:
        print("Fecha inválida.")

###Bloque principal
main()