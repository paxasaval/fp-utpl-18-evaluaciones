def main():
    segundos = eval(input("Ingrese la cantidad de segundos: "))

    minutos = segundos // 60
    residuo = segundos % 60

    print(segundos, " segundos es igual a ", minutos, " minuto(s) y ", residuo, " segundos")


main()
