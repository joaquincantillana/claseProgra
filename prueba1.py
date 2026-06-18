def buscar_mascota(lista_m, nombre_m):

    for x in range(len(lista_m)):
        if nombre_m == lista_m[x]["nombre"]:
            return x
    return -1
        
def validar_nombre(nombre):


    return nombre.strip() != ""
 
def validar_especie(especie):

    especies_validas = ["perro","gato","ave"]
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    
    return edad.isdigit() and int(edad) > 0

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
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Debe de ingresar un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe de ingresar un numero")
    return opcion

def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacio")
        return

    especie = input("Ingrese la especie de la mascota (perro, gato o ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie solo puede ser perro, gato o ave")
        return

    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La edad debe de ser un numero entero mayor a cero")
        return

    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
        }
    lista.append(mascota)
    print("Mascota agregada correctamente")

def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False


lista_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()
    if op == 1:
        agregar_mascota(lista_mascotas)

    elif op == 2:
        print("****Buscar mascota****")
        nombre = input("Ingrese el nombre de la mascota: ")
        posicion = buscar_mascota(lista_mascotas , nombre)
        if posicion != -1:
            print(f"la posicion encontrada es: {posicion + 1}")
            m = lista_mascotas[posicion]
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"Especie mascota: {m["especie"]}")
            print(f"Edad mascota: {m["edad"]}")
            print(f"Vacunada: {m["vacunada"]}")
        else:
            print("la mascota no se ha encontrado")

    elif op == 3:
        print("****Eliminar mascota****")
        nombre = input("Ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(lista_mascotas , nombre)
        if posicion != -1:
            lista_mascotas.pop(posicion)
            print("La mascota ha sido eliminada de la lista")
        else:
            print(f"La mascota {nombre} no se encuentra la lista")


    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("vacuna actualizada")

    elif op == 5:
        actualizar_vacunas(lista_mascotas)
        if len(lista_mascotas) == 0:
            print("No hay mascotas en la lista")
        else:
            print("== lista de mascotas == ")
            for m in lista_mascotas:
                print(f"Nombre: {m["nombre"]}")
                print(f"Especie: {m["especie"]}")
                print(f"Edad: {m["edad"]}")
                estado = "AL DIA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado vacuna: {estado}")
                print("======================")
    elif op == 6:
        print("Gracias por usar el sistema")

    











