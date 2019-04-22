"""
	Ejemplo de lenguajes en python
"""


import sys

nombre = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

suma = int(valor1) + int(valor2) # aqui realizo la suma de variables

mutli = int(valor1) * int(valor2)

print("La suma es: %d" % suma)