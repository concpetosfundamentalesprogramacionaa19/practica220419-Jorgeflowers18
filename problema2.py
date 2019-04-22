"""
	En este archivo tipo py vamos a realizar el problema 2
	, el cual pide el ingreso de variables en modo strin y 
	luego convertirlos a enteros para realizar una 
	operación con el
"""
# Ingreso y petición de variables

x = input("Por favor ingresa la variable x: ")
y = input("Por favor ingresa la variable y: ")
z = input("Por favor ingresa la variable z: ")
"""
	En python viene por defecto el tipo String por lo tanto
	en la operación hay que transformarlo a enteros
"""

x = float(x) 
y = float(y) 
z = float(z) 
# aquí va la operación
 
m = (x + (y / z)) / (x - (y / z))

 

# Ahora solo hay que presentar la variable que el resultado

print("El valor de m, en base a las variables:\nx=%.1f\n\
	y=%.1f\n\t\tz=%.1f\nda como resultado:\n\t\t\tm=%.1f\n" 
% (x, y, z, m))