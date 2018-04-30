def main():
    c1 = eval(input("Ingrese la priemra calificacion del alumno: "))
    c2 = eval(input("Ingrese la segunda calificacion del alumno: "))
    c3 = eval(input("Ingrese la tercera calificacion del alumno: "))
    c4 = eval(input("Ingrese la cuarta calificacion del alumno: "))

    promedio = (c1 + c2 + c3 + c4) / 4

    if promedio <= 100 and promedio >= 90:
        puntuacion = "A"
    elif promedio <= 89 and promedio >= 80:
        puntuacion = "B"
    elif promedio <= 79 and promedio >= 70:
        puntuacion = "C"
    elif promedio <= 69 and promedio >= 0:
        puntuacion = "D"
    else:
        print("Error al calcular la puntuacion del alumno")

    print("El estudiante con el promedio de calificaciones", promedio, "tiene una puntuación de", puntuacion,".")

main()
