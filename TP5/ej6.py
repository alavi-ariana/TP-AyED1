def ingresar_num() -> list:
    listorta = []
    while True:
        try:
            num = int(input("Ingrese los números a agregar: "))
            if num == -1:
                break
            listorta.append(num)
        except ValueError:
            print("Debe ingresar datos válidos.")
    return listorta

def sacar_indice(lista):
    errores = 0
    while errores < 3:
        print(errores)
        try:
            num = int(input("Ingrese el número para sacar su indice: "))
            print(f"El número {num} está en el indice {lista.index(num)}.")
        except ValueError as e:
            if errores == 3:
                break
            errores += 1
            print(e)
    print("Se hicieron 3 errores. Bye!")

def main() -> None:
    lista = ingresar_num()
    print(lista)
    sacar_indice(lista)

if __name__ == "__main__":
    main()

# End-of-file (EOF)
