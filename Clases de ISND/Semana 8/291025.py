"""¿qué pasa mientars este conectado? literal se va ejecutando mientras la condicion que le damos es verdadera. 
###1
ejecución = True
while ejecución: 
    opción = input("¿Estamos ejecutando el menú? Y/N: ")   # <- hasta aquí es un bucle infinito
    if opción.lower() == "n": 
        ejecución = False  #<- aquí si ya se va parar porque el mismo usuario
    elif opción.lower() == "y":
        print("les kip goin") #si quiero, puedo volver a colocar el estado de arriba pues el programa seguira ejecutandose
    else: 
        print("La opción elegida no es valida. ")
        
print("Grcias por utilizar nuestro sistema") 



###2 Un sistema de registro  -< con for - cuando se cuanto es el maximo
alumnos = 0
lista_alumno = []
cantidad = int(input("¿Cuántos alumnos voy a ingresar?"))
for i in range(cantidad): 
    alumno = input("Digite el nombre del alumno: ")
    lista_alumno.append(alumno)
print (lista_alumno)"""

###3 con while
alumnos = 0
lista_alumno = []

print("Bienvenido a nuestro sistema de control de alumnos. ")
menu = True
while menu: 
    opción = input("Elija la opción:  (1: ingresar alumnos, 2: Consultar, 3: Modificar, 4: Eliminar, 5: Salir,): ")
    if opción == "1": 
        print("Vamos a ingresar alumnos: ")
        alumno = input("Digite el nombre del alumno: ")
        lista_alumno.append(alumno)
    elif opción == "2": 
        print(lista_alumno)
    elif opción == "5":
        menu = False
    elif opción == "3": 
        posición = int(input("Ingrese la posición del alumno: "))
        name = input("Ingrese el nuevo nombre: ")
        lista_alumno[posición-1] = name
    elif opción == "4": 
        borrado = lista_alumno.pop(int(input("Inserte el alumno que quiere eliminar (1-4): "))-1)
        print(f"Usted ha matado a {borrado}. ")
    else: 
        print("Esa opción no existe, checa eso porfa")
        
        
print("Haz salido del menú")


### TENGO QUE SALIRME DEL WHILE, ES DECIR HACER Q LA CONDICION SE TERMINE PARA QUE SE ACTUALICE LA TERMINAL
    