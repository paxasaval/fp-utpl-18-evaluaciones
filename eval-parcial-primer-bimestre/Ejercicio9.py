def main():
    a1 = eval(input("Ingrese un lado del triangulo A: "))
    b1 = eval(input("Ingrese un lado del triangulo A: "))
    c1 = eval(input("Ingrese un lado del triangulo A: "))
    x1 = eval(input("Ingrese un angulo del triangulo A: "))
    y1 = eval(input("Ingrese un angulo del triangulo A: "))
    z1 = eval(input("Ingrese un angulo del triangulo A: "))
    a2 = eval(input("Ingrese un lado del triangulo B: "))
    b2 = eval(input("Ingrese un lado del triangulo B: "))
    c2 = eval(input("Ingrese un lado del triangulo B: "))
    x2 = eval(input("Ingrese un angulo del triangulo B: "))
    y2 = eval(input("Ingrese un angulo del triangulo B: "))
    z2 = eval(input("Ingrese un angulo del triangulo B: "))

    lados_A = [a1, b1, c1]
    lados_B = [a2, b2, c2]
    angulos_A = [x1, y1, z1]
    angulos_B = [x2, y2, z2]

    def ordenar_lista(lista):
        for i in range(0, len(lista), 1):
            for j in range(i, len(lista), 1):
                if lista[j] >= lista[i]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return (lista)

    lados_A = ordenar_lista(lados_A)
    lados_B = ordenar_lista(lados_B)
    angulos_A = ordenar_lista(angulos_A)
    angulos_B = ordenar_lista(angulos_B)
    if lados_A == lados_B and angulos_A == angulos_B:
        print("Los triangulos son congruentes")
    else:
        print("Los triangulso NO son congruentes")


main()
