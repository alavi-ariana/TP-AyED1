"""Programa para llevar registro de socios de un club."""
def registrar(socio: int) -> dict[int, int]:
    """ Registra el ingreso de un socio al club, incrementando la cantidad de veces que entra.
        Returns:
            - Si el socio ya está registrado, incrementa su conteo de ingresos.
            - Si es un socio nuevo, lo agrega al club con un valor inicial de 1.
            - Devuelve el diccionario club.
    """
    if socio in club:
        club[socio] += 1
    else:
        club[socio] = 1
    return club

def veces_en_club() -> None:
    """Imprime cuántas veces cada socio ha ingresado en el club."""
    for socio, veces in club.items():
        print(f"SOCIO: {socio} ingresó {veces} veces")

def opciones():
    print("1) Ingresar socio")
    print("2) Informe por cada socio cuántas veces ingresó al club")
    print("3) Baja del club")
    print("4) Salir")

if __name__ == "__main__":
    club = {}
    while True:
        opciones()
        op = input("Ingrese su opción: ")
        match op:
            case "1":
                while True:
                    try:
                        socio = int(input("Ingrese número de socio (5 dígitos o 0 para salir): "))
                        if socio == 0:
                            break
                        if len(str(socio)) == 5:
                            club = registrar(socio)
                        else:
                            print("Ingrese 5 dígitos.")
                    except ValueError:
                        print("Sólo números enteros.")
            case "2":
                if not club:
                    print("No hay socios.")
                else:
                    veces_en_club()
            case "3":
                if not club:
                    print("No hay socios.")
                else:
                    print("SOCIOS DEL CLUB")
                    for socios, valor in club.items():
                        print(f"{socios}")
                    try:
                        socio_baja = int(input("Ingrese el número de socio que se dio de baja: "))
                        if socio_baja in club:
                            ingresos_eliminados = club.pop(socio_baja)
                            print(f"Socio {socio_baja} eliminado con {ingresos_eliminados} ingresos eliminados.")
                        else:
                            print("El número de socio no se encontró en los registros.")
                    except ValueError:
                        print("Número inválido.")
            case "4":
                break
            case _:
                print("Opción no válida.")

# End-of-file (EOF)

