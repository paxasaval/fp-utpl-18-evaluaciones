def main():
    a = eval(input("Ingrese el valor de (a): "))
    b = eval(input("Ingrese el valor de (b): "))
    c = eval(input("Ingrese el valor de (c): "))
    d = eval(input("Ingrese el valor de (d): "))
    e = eval(input("Ingrese el valor de (e): "))
    f = eval(input("Ingrese el valor de (f): "))

    x = ((c * e - b * f) / (a * e - b * d))
    y = ((c * e - b * f) / (a * e - b * f))

    print("Dado el siguiente sistema de ecuaciones: ")
    print(a, "x + ", b, "y = ", c)
    print(d, "x + ", e, "y = ", f)
    print("Los valores de las variables (x) y (y) son:")
    print("x = ", x)
    print("y = ", y)


main()
