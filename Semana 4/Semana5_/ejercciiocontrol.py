###1
"""Enero = int(input("Digite las cantidades de Enero: "))
Febrero = int(input("Digite las cantidades de Febrero: "))
Marzo = int(input("Digite las cantidades de Marzo: "))


costo = Enero*1.2 + Febrero*1.38 + Marzo*1.14"""

#print(f"""La cantidad de artículos producidos fue: {Enero} en Enero, {Febrero} febrero y {Marzo} en Marzo. 
#el costo total fue de ${costo: .2f}""")

##2
"""Días = ["lunes", "martes", "miércoles", "jueves", "viernes"] #Ojo con colocarle mayusculas y escribir igual el tetxo de aca de la lista con lo que coloco en el input
Lu = int(input("Lunes: "))
Días [0] = Lu
print(f"El día Lunes se vendieron {Lu} productos")   #Para modificar el dato que esta dentro de la lista
Mar = int(input("Martes: "))
Días [1] = Mar
print(f"El día Martes se vendieron {Mar} productos")   #Para modificar el dato que esta dentro de la lista
Mier = int(input("Miércoles: "))
Días [2] = Mier
print(f"El día Miércoles se vendieron {Mier} productos")   #Para modificar el dato que esta dentro de la lista
Jue = int(input("Jueves: "))
Días [3] = Jue
print(f"El día Jueves se vendieron {Jue} productos")   #Para modificar el dato que esta dentro de la lista
Vie = int(input("Viernes: "))
Días [4] = Vie
print(f"El día Viernes se vendieron {Vie} productos")#Para modificar el dato que esta dentro de la lista
print(f"la producción de la semana fue {Lu+Mar+Mier+Jue+Vie}")
print(f"Lista actualizada:{Días} ")"""

###3
"""frutas = [1, 2, 3, 4, 5, 6]
niño1 = input("¿Cuál es tu fruta fav?")
frutas[0] = niño1
print(frutas)
niño1 = input("¿Cuál es tu fruta fav?")
frutas[1] = niño1
print(frutas)
niño1 = input("¿Cuál es tu fruta fav?")
frutas[2] = niño1
print(frutas)
niño1 = input("¿Cuál es tu fruta fav?")
frutas[3] = niño1
print(frutas)
niño1 = input("¿Cuál es tu fruta fav?")
frutas[4] = niño1
print(frutas)
niño1 = input("¿Cuál es tu fruta fav?")
frutas[5] = niño1
print(f"las frutas favoritas de los  niños son: {frutas}")"""

### 4
"""alumnos = ("Diego", "Paquito", "Calvito", "Aby", "Alvin", "Medranito", "Gene")
alumnito = int(input("Ingrese el orden de niño que desea saber (1-7):"))
print(f"El alumno que ingreso como numero {alumnito} es {alumnos[alumnito-1]}")"""
##5
"""nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = "@isnd.com"

#propuesta1 = nombre.lower() + "."+ apellido.lower() + dominio
#propuesta2 = nombre[0].lower() + apellido.lower() + dominio

print(f"Propuesta 1: {nombre.lower()}.{apellido.lower()}{dominio}")
print(f"Propuesta 2: {nombre[0].lower()}.{apellido.lower()}{dominio}")"""

###6
monto = input("Ingrese su monto: ") #in para ver si esta o no esta
print("$" in monto)
print(monto.count("$")==1) 
print(monto[0] == "$")

###7
#2 letras aleatorias
palabra = "dfgupccbjkaj"