"""
	En este archivo tipo py vamos a realizar el problema 1
	, el cual pide el ingreso de variables en modo strin y 
	luego convertirlos a enteros para realizar una 
	operación con el
"""
# Ingreso y petición de variables

numhoras = float(input("Por favor ingrese el número de horas\
que ha acumulado el trabajador: "))
costhora = float(input("Por favor ingrese el costo por hora: "))
 

# aquí van las operaciones



aux = numhoras * costhora

aux2 = aux * 0.1

sueldo = aux - aux2



# Ahora solo hay que presentar las variables

print("El sueldo mensual final a pagar es: %.2f\n y el\
	valor descontado por el Seguro Social es: %.2f" 
	% (sueldo, aux2)) 