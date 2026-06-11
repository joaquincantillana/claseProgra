def mostrar_encabezado():
    print("---------------")
    print("|| Sistema de admision Escolar ||")
    print("----------------")
def solicitar_datos():
    estudiante = {}
    estudiante["rut"] = input("Ingrese el rut del estudiante: ")
    estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    estudiante["carrera"] = input("Ingrese la carrera del estudiante: ")
    while True:
        try:
            estudiante["semestre"] = int(input("Ingrese el semestre del estudiante: "))
            if estudiante["semestre"] < 1 or estudiante["semestre"] > 4:
                print("debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("Debe de ingresar un numero")
    return estudiante

def mostrar_datos(alumnos):
    print(f"Nombre del estudiante: {alumnos["nombre"]}")
    print(f"Rut del estudiante: {alumnos["rut"]}")
    print(f"Carrera del estudiante: {alumnos["carrera"]}")
    print(f"Semestre del estudiante: {alumnos["semestre"]}")

datos = solicitar_datos()

mostrar_encabezado()
mostrar_datos(datos)
