"""Module dosctring"""
def ascendente(lista: list) -> bool:
    """Verifica si una lista está ordenada ascendentemente.
        Returns:
            - bool: True si la lista está ordenada, caso contrario False."""
    return lista == sorted(lista)

if __name__ == "__main__":
    while True:
        listorta = []
        print("CREE SU LISTA 1) Int 2) Str")
        op = input("Ingrese su opción: ")
        match op:
            case "1":
                try:
                    while True:
                        valor_int = int(input("Ingrese los enteros(-1 para salir): "))
                        if valor_int == -1:
                            break
                        listorta.append(valor_int)
                except ValueError:
                    print("Solo enteros.")
            case "2":
                while True:
                    valor_str = input("Ingrese los elementos cadena(-1 para salir): ")
                    if valor_str == "-1":
                        break
                    listorta.append(valor_str)
            case _:
                print("Opción no válida.")
        print(listorta)
        print(f"El valor de lista ordenada es: {ascendente(listorta)}")

# End-of-file (EOF)
