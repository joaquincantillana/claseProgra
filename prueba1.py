def mostrar_menu():
    print("------MENU PRINCIPAL---------------")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar mascotas")
    print("6.- Salir")
    print("---------------------")
    
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion"))
            if opcion < 1 or opcion > 6:
                print("Debe de ingresar un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe de ingresar un numero")
    return opcion

lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()












