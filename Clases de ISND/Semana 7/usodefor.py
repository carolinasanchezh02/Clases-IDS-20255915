## declaración basica de For y range
"""for i in range(5): 
	print(f"El valor de i es: {i}. ")
	
for i in range(3, 7): 
 print(f"i vale {i}.")
 
#for con listas
colores = ["azul", "amarillo", "rojo"]
print("listado de colores")
for color in colores: 
	print(f"El color es: {color}")

#for cuando quiero que omita elementos de mi lista 
colores = ["azul", "amarillo", "rojo"]
print("listado de colores")

for color in colores: 
	if color == "azul":
		print("Se ha saltado el color azul") #este indicador debe estar antes del continue, que sería lo ultimo
		continue  #esto hace que se salte la ejecución
	print(f"El color es: {color}")"""
 
 #for cuando quiero que termine de ejecutr antes de cierto valor
colores = ["azul", "amarillo", "rojo"]
print("listado de colores")

for color in colores: 
		if color == "azul":
				print("Se ha roto la ejecución del bucle") #este indicador debe estar antes del continue, que sería lo ultimo
				break #rompe la ejecución. finaliza completamente
		print(f"El color es: {color}")
