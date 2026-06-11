def conversion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total ) + 1
    return round(nota, 1)

while True:
    try:
        p = float(input("Ingrese la nota del estudiante: "))
        if p < 0:
            print("debe de ingresar un numero positivo")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")
while True:
    try:
        pt = float(input("Ingrese la nota final de la evaluacion: "))
        if pt < 0:
            print("debe de ingresar un numero positivo")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")
calif = conversion_notas(p, pt)
print(f"La nota chilena es : {calif}")


