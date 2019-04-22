"""	
	Ejemplo 3 de lenguaje python
"""
# Con el comando input introducimos en una sola linea la variable y presentamos el texto

num1 = input("Ingrese por favor el dato 1: ")
num2 = input("Ingrese por favor el dato 2: ")

# Aqui se realiza la operación con las caribales transformandolas a enteros

suma = int(num1) + int(num2) # aqui realizo la suma de variables

multi = int(num1) * int(num2)

# Aquí se presenta la variable final en un comand print

print("La suma es: %d\ty la multiplicación es: %d" % (suma, multi))



