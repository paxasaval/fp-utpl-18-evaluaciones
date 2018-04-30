def main():
    v1 = (input("Ingrese una letra del alfabeto: "))
    v2 = input("Ingrese una letra del alfabeto: ")
    v3 = input("Ingrese una letra del alfabeto: ")

    def letra_a_numero(x):
        if x == ("a" or "A"):
            y = 1
        elif x == ("b" or "B"):
            y = 2
        elif x == ("c" or "C"):
            y = 3
        elif x == ("d" or "D"):
            y = 4
        elif x == ("e" or "E"):
            y = 5
        elif x == ("f" or "F"):
            y = 6
        elif x == ("g" or "G"):
            y = 7
        elif x == ("h" or "H"):
            y = 8
        elif x == ("i" or "I"):
            y = 9
        elif x == ("j" or "J"):
            y = 10
        elif x == ("k" or "K"):
            y = 11
        elif x == ("l" or "L"):
            y = 12
        elif x == ("m" or "M"):
            y = 13
        elif x == ("n" or "N"):
            y = 14
        elif x == ("o" or "O"):
            y = 15
        elif x == ("p" or "P"):
            y = 16
        elif x == ("q" or "Q"):
            y = 17
        elif x == ("r" or "R"):
            y = 18
        elif x == ("s" or "S"):
            y = 19
        elif x == ("t" or "T"):
            y = 20
        elif x == ("u" or "U"):
            y = 21
        elif x == ("v" or "V"):
            y = 22
        elif x == ("w" or "W"):
            y = 23
        elif x == ("x" or "X"):
            y = 24
        elif x == ("y" or "Y"):
            y = 25
        elif x == ("z" or "Z"):
            y = 26
        else:
            print("Error")
        return (y)

    n1 = letra_a_numero(v1)
    n2 = letra_a_numero(v2)
    n3 = letra_a_numero(v3)
    if n1 <= n2 and n1 <= n3:
        menor = v1
    elif n2 <= n1 and n2 <= n3:
        menor = v2
    elif n3 <= n1 and n3 <= n2:
        menor = v3

    print("La primera letra que aparece en el abecedario es ", menor)


main()
