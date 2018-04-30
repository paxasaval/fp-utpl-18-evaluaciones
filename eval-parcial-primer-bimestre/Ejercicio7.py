def main():
    sueldo_base = 360.40
    ventas = eval(input("Ingrese el valor de las ventas: "))
    if ventas <= 500:
        bono = 0.05
    elif ventas > 500 and ventas <= 1000:
        bono = 0.08
    elif ventas > 1000 and ventas <= 5000:
        bono = 0.10
    else:
        bono = 0.15
    salario = sueldo_base + (ventas * bono)
    print("El empleado con un total de ventas de", ventas, "recibe un sueldo por", salario, "el presente mes.")


main()
