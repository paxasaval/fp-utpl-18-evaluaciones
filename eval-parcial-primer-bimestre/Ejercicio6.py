def main():
    mes=eval(input("Ingrese el numero de un mes (1-12): "))

    if mes in [1,3,5,7,8,10,12]:
        dia=31
    elif mes in [4,6,9,11]:
        dia=30
    elif mes==2:
        dia=28
    else:
        print("El numero ingresado no corresponde a ningun mes")
    print("El", mes,"mes del año tiene",dia,"dias.")
main()
