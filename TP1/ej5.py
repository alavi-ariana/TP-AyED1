"""Funciones para determinar si un número es oblongo y triangular."""

oblongo = lambda num: any(num == k * (k + 1) for k in range(1, int(num ** 0.5) + 1 ))

triangular = lambda num: any(num == k * (k + 1) // 2 for k in range(1, int((2 * num) ** 0.5) + 1))

while True:
    try:
        op_oblongo = int(input("OBLONGO | Ingrese su número: "))
        op_triangular = int(input("TRIANGULAR | Ingrese su número: "))
        if op_oblongo > 0 and op_triangular > 0:
            break
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Solo números enteros.")
        continue

if oblongo(op_oblongo):
    print("Es oblongo.")
else:
    print("No es oblongo.")

if triangular(op_triangular):
    print("Es triangular.")
else:
    print("No es triangular.")
#End-of-file (EOF)
