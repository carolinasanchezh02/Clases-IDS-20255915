#Para que puesa regsitrar estudiantes
def registrar_estudiante(lista_estudiantes):
    """Para registrar los datos del estudiante"""
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
    print(f"Tu carnte es {estudiante["carnet"]}")

#para que muestre la lista de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    "Para mostrar los datos del estudiante"
    for est in lista_estudiantes:
        print(est)