def buscar_reserva(lista_r, huesped):

    for x in range(len(lista_r)):
        if huesped == lista_r[x]["huesped"]:
            return x
    return -1

def validar_huesped(huesped):

    return huesped.strip() != ""

def validar_habitacion(habitacion):

    return habitacion.isdigit() and int(habitacion)  >= 1 and int(habitacion) <= 200

def validar_noches(noches):

    return noches.isdigit() and int(noches) > 0


def mostrar_menu():

    print("------MENU PRINCIPAL---------------")

    print("1.- Agregar reserva")

    print("2.- Buscar reserva")

    print("3.- Eliminar reserva")

    print("4.- Confirmar reservas")

    print("5.- Mostrar reservas")

    print("6.- Salir")

    print("---------------------")


def ingresar_opcion():

    while True:

        try:

            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 6:
                print("Debe ingresar un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return opcion

def agregar_reserva(lista):   

    huesped = input("Ingrese el nombre del huesped: ")

    correcto = validar_huesped(huesped)

    if not correcto:

        print("El nombre no puede estar vacio")
        return

    habitacion = input("Ingrese el numero de habitacion: ")

    correcto = validar_habitacion(habitacion)

    if not correcto:

        print("La habitacion debe estar entre 1 y 200")
        return

    noches = input("Ingrese la cantidad de noches: ")

    correcto = validar_noches(noches)

    if not correcto:

        print("Las noches deben ser mayores a cero")
        return

    reserva = {

        "huesped": huesped.strip(),
        "habitacion": int(habitacion),
        "noches": int(noches),
        "confirmada": False
    }

    lista.append(reserva)

    print("Reserva agregada correctamente")


def confirmar_reservas(lista_r):

    for r in lista_r:

        if r["noches"] >= 2:

            r["confirmada"] = True

        else:

            r["confirmada"] = False
def mostrar_reservas(lista_r):
    print("---- Lista de resservas--")
    for i in lista_r:
        print(f"Huesped: {i['huesped']}")
        print(f"Habitacion: {i['habitacion']}")
        print(f"Noches: {i['noches']}")
        print(f"Confirmada: {i['confirmada']}")
        if i ["confirmada"]:
            print("estado: confirmada")
        else:
            print("estado : pendiente")
        print("-------------")
lista_reservas = []

op = 0

while op != 6:

    mostrar_menu()

    op = ingresar_opcion()

    if op == 1:

        agregar_reserva(lista_reservas)

    elif op == 2:

        print("****Buscar reserva****")

        huesped = input("Ingrese el nombre del huesped: ")

        posicion = buscar_reserva(lista_reservas, huesped)

        if posicion != -1:

            print(f"La posicion encontrada es: {posicion + 1}")

            r = lista_reservas[posicion]

            print(f"Huesped: {r['huesped']}")

            print(f"Habitacion: {r['habitacion']}")

            print(f"Noches: {r['noches']}")

            print(f"Confirmada: {r['confirmada']}")

        else:

            print("La reserva no se ha encontrado")

    elif op == 3:

        print("****Eliminar reserva****")

        huesped = input("Ingrese el nombre del huesped a eliminar: ")

        posicion = buscar_reserva(lista_reservas, huesped)

        if posicion != -1:

            lista_reservas.pop(posicion)

            print("La reserva ha sido eliminada")

        else:

            print(f"La reserva del huesped {huesped} no se encuentra registrada")

    elif op == 4:

        confirmar_reservas(lista_reservas)

        print("Reservas actualizadas")

    elif op == 5:

        confirmar_reservas(lista_reservas)

        if len(lista_reservas) == 0:

            print("No hay reservas en la lista")

        else:

            print("=== LISTA DE RESERVAS ===")

            for r in lista_reservas:

                print(f"Huesped: {r['huesped']}")

                print(f"Habitacion: {r['habitacion']}")

                print(f"Noches: {r['noches']}")

                estado = "CONFIRMADA" if r["confirmada"] else "PENDIENTE"

                print(f"Estado: {estado}")

                print("======================")

    elif op == 6:

        print("Gracias por usar el sistema. Vuelva pronto")
