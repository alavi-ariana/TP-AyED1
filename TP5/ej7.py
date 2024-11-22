import random as rn

def generar_num(min_: int, max_: int) -> int:
    """ Genera un número al azar entre el minimo y el maximo.
        Args:
            - min_: int, no debe ser vacio.
            - max_: int, no debe ser vacio.
        Returns:
            - int: el número al azar.
    """
    return rn.randint(min_, max_)

def ask_guess() -> int:
    """Solicita un input al usuario e intenta castearlo para devolverlo en entero.
    Args:
        - None
    Return:
        - int: número del usuario en formato entero.
    """
    try:
        return int(input("INGRESE SU GUESS: "))
    except ValueError:
        print("Debe ingresar un número entero.")
    except KeyboardInterrupt:
        print("Saliendo...")

def main() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    num = generar_num(1, 501)
    intentos = 0
    while True:
        try:
            op_guess = ask_guess()
            if op_guess == num:
                intentos += 1
                break
            elif op_guess > num:
                print("Menor")
                raise ValueError
            elif op_guess < num:
                print("Mayor")
                raise ValueError
        except ValueError:
            intentos += 1
        except TypeError:
            intentos += 1

    print(f"USTED ADIVINÓ EL NÚMERO! La cantidad de intentos fue de {intentos} {'vez' if intentos == 1 else 'veces'}")

if __name__ == "__main__":
    main()

# End-of-file (EOF)
