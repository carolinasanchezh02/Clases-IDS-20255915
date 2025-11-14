print("Vamos a registrar un estudiante: ")
#Para que puesa regsitrar estudiantes
def registrar_estudiante(lista_estudiantes):
    estudiante = {}
    num = len(lista_estudiantes) + 1
    if num < 10:
        carnet = "S00" + str(num)
    elif num < 100:
        carnet = "S0" + str(num)
    else:
        carnet = "S" + str(num)
    estudiante["carnet"] = carnet
    estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    lista_estudiantes.append(estudiante) 

#para que muestre la lista de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    for est in lista_estudiantes:
        print(est)