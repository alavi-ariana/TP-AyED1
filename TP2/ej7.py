""" Intercalar los elementos de una lista entre los elementos de otra.
    Mediante el uso de slice()"""

def intercalar(lista1: list[int], lista2: list[int]) -> None:
    """ Intercambia elementos entre dos listas"""
    len_mas_corto = min(len(lista1), len(lista2))

    for i in range(len_mas_corto):
        lista1[2 * i + 1:2 * i + 1] = [lista2[i]]

    if len(lista2) > len_mas_corto:
        lista1.extend(lista2[len_mas_corto:])


if __name__ == "__main__":
    onelist: list = []
    twolist: list = []
    while True:
        print(onelist)
        print(twolist)
        op = input("Seleccione lista a llenar 1 o 2 (-1 para salir): ")
        match op:
            case "1":
                try:
                    while True:
                        num = int(input("Ingrese los números(-1 para salir): "))
                        if num == -1:
                            break
                        onelist.append(num)
                except ValueError:
                    print("Solo enteros.")
            case "2":
                try:
                    while True:
                        num = int(input("Ingrese los números(-1 para salir): "))
                        if num == -1:
                            break
                        twolist.append(num)
                except ValueError:
                    print("Solo números enteros.")
            case "-1":
                break
            case _:
                print("Opción no válida.")
    print(onelist)
    print(twolist)
    intercalar(onelist, twolist)
    print(f"Lista intercalada: {onelist}")

# End-of-file (EOF)
