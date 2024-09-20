"""programa para crear una baraja de los cuatro palos mediante lista por comprensión"""
if __name__ == "__main__":
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    baraja = [f"{numeros} {palo}" for palo in palos for numeros in range(1, 13)]
    print(baraja)