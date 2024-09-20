""" Programa para generar una lista con números al azar entre 1 y 100,
    otra con los elementos impares de la primera lista usando filter()"""

if __name__ == "__main__":
    lista = [num for num in range(1, 100)]
    lista2 = list(filter(lambda x: x % 2 != 0, lista))
    print(f"Lista original: {lista}")
    print(f"Lista filtrada: {lista2}")

# End-of-file (EOF)
