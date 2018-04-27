def main():
	x=eval(input("Ingrese el valor para la variable (x)"))
	y=eval(input("Ingrese el valor para la variable (y)"))
	z=eval(input("Ingrese el valor para la variable (z)"))
	
	m=((x+(y/z))/(x-(y/z)))
	
	print("El Valor de m en base a las variables: ")
	print("x = ", x)
	print("y = ", y)
	print("z = ", z)
	print("da como resultado: ")
	print("m = ", m)
main()