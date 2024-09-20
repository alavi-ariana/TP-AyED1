"""Programa para clínica."""
def busqueda(busqueda: int) -> tuple:
    """Busca el número de afiliado en el registro de la clínica y cuenta
        cuántas veces fue atendido por urgencia o turno."""
    urgencias, turno = 0, 0
    for clave, valor in clinica:
        if busqueda == clave:
            if valor == 0:
                urgencias += 1
            elif valor == 1:
                turno += 1
    return urgencias, turno

def atendidos(caso: int) -> set:
    """Devuelve un conjunto de los números de afiliado atendidos según el tipo de caso."""
    atendidos = set()
    for paciente, situacion in clinica:
        if situacion == caso and paciente not in atendidos:
            atendidos.add(paciente)
    return atendidos

if __name__ == "__main__":
    clinica: list[tuple] = []
    while True:
        print("\n1) Ingresar número de afiliado")
        print("2) Mostrar un listado de los pacientes atendidos en el orden que llegaron a la clínica.")
        print("3) Buscar un afiliado y ver cuántas veces fue atendido")
        print("4) Salir")
        op = input("Elegir opción: ")
        match op:
            case "1":
                while True:
                    try:
                        op_afiliado = int(input("Ingrese número de afiliado(-1 para salir): "))
                        if op_afiliado == -1:
                            break
                        if len(str(op_afiliado)) == 4:
                            try:
                                situacion = int(input("Indique si viene de urgencia (0) o con turno (1): "))
                                if situacion in [0, 1]:
                                    clinica.append((op_afiliado, situacion))
                                else:
                                    print("Opción no válida.")
                            except ValueError:
                                print("Debe poner un valor entero.")
                        else:
                            print("El nro de afiliado debe ser de 4 dígitos.")
                    except ValueError:
                        print("Números enteros.")
            case "2":
                atendidos_urgencia = atendidos(0)
                if atendidos_urgencia:
                    print("PACIENTES ATENDIDOS POR URGENCIA")
                    for paciente in atendidos_urgencia:
                        print(f"Nro de afiliado: {paciente}")
                else:
                    print("No hay pacientes atendidos en URGENCIA")
                atendidos_turno = atendidos(1)
                if atendidos_turno:
                    print("PACIENTES ATENDIDOS POR TURNO")
                    for paciente in atendidos_turno:
                        print(f"Nro de afiliado: {paciente}")
                else:
                    print("No hay pacientes atendidos en TURNO")
            case "3":
                while True:
                    try:
                        search = int(input("Ingrese número de afiliado a buscar(-1 para salir): "))
                        if search == -1:
                            break
                        if len(str(search)) == 4:
                            urgencias, turnos = busqueda(search)
                            if urgencias == 0 and turnos == 0:
                                print("El paciente no fue atendido.")
                            else:
                                print(f"El paciente {search} fue atendido URGENCIAS: {urgencias} - TURNO: {turnos}")
                        else:
                            print("Número afiliado de 4 dígitos.")
                    except ValueError:
                        print("Solo números enteros.")
            case "4":
                break
            case _:
                print("Opción no válida.")

# End-of-file (EOF)
