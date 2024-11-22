def imprimir_num() -> None:
    """Imprime los números del 1 al 1000000 hasta que el usuario le indique
        o termine de imprimirlos el programa primero.
        Args: None
        Returns: None
    """
    exit_ = False
    while not exit_:
        for num in range(1, 100001):
            try:
                if exit_:
                    break
                print(num)
            except KeyboardInterrupt:
                op = input("¿Desea parar el programa? (Y/N): ")
                if op.lower() == "y":
                    exit_ = True

if __name__ == "__main__":
    imprimir_num()

# End-of-file (EOF)
