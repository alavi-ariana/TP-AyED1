""" programa"""
def num_to_letras(num: int) -> str:
    """ Convierte un entero  entre 0 y 1 billón en su representación en letras"""
    dict_letras = {
            0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
            6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez",
            11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
            16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
            20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
            60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa",
            100: "cien", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos",
            500: "quinientos", 600: "seiscientos", 700: "setecientos",
            800: "ochocientos", 900: "novecientos", 1000: "mil"
        }

    if num < 21:
        return dict_letras[num]

    if num < 100:
        decena = (num // 10) * 10
        unidad = num % 10
        return dict_letras[decena] + (("y" + dict_letras[unidad]) if unidad > 0 else " ")

    if num < 1000:
        centena = (num // 100) * 100
        resto = num % 100
        if num == 100:
            return "cien"
        else:
            return dict_letras[centena] + ((" " + num_to_letras(resto)) if resto > 0 else " ")

    if num < 1_000_000:
        if num == 1000:
            return "mil"
        mil = num // 1000
        resto = num % 1000
        if mil == 1:
            return "mil" + ((" "+ num_to_letras(resto)) if resto > 0 else " ")
        else:
            return (num_to_letras(mil) + "mil" + ((" " + num_to_letras(resto)) if resto > 0 else " "))

    if num < 1_000_000_000:
        millon = num // 1_000_000
        resto = num % 1_000_000
        if millon == 1:
            return "un millon" + ((" "+ num_to_letras(resto)) if resto > 0 else " ")
        else:
            return num_to_letras(millon) + "millones" + ((" "+ num_to_letras(resto)) if resto > 0 else " ")

    if num < 1_000_000_000_000:
        mil_millon = num // 1_000_000_000
        resto = num % 1_000_000_000
        if mil_millon == 1:
            return "mil millones" + ((" "+num_to_letras(resto)) if resto > 0 else " ")
        else:
            return num_to_letras(mil_millon) + "mil millones" + ((" " + num_to_letras(resto)) if resto > 0 else " ")

    return " "

if __name__ == "__main__":
    numero = int(input("Ingrese un número entre 0 y 1 billón: "))
    if numero >= 0 and numero <=1_000_000_000_000:
        print(num_to_letras(numero))
    else:
        print("Número fuera de rango.")

# End-of-file (EOF)
