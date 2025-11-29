"""colores = {
    "primario": "rojo",
    "secundario": "verde",
    "bandera": "rojo",
    "extra": "amarillo",
    "decoracion": "verde"
}

repetidos = []
colors = list(colores.values())
for n in colors: 
    if colors.count(n)>1 and n not in repetidos: 
        repetidos.append(n)
print(f"Los colores repetidos son: {repetidos}") 

for key in colores: 
    for keys in colores: 
        if key != keys:
            if colores[key] == colores[keys]:
                print(f"{key} - {keys}")
def operacion(a, b):
    return a*b, a+b   # devuelve una tupla

prod, suma = operacion(4,5)
print(prod, suma)"""

"""
Si quieres, envíame tus soluciones y las reviso."""

#1 Escribe registrar_estudiante(lista): pide nombre, genera carnet S + número y guarda en lista.
"""lista = []
def registrar_estudiante(lista):
    estudiante = {}
    nombre = input("Ingrese su nombre: ")
    numero = len(lista) + 1
    if numero < 10: 
        carnet = "S00" + str(numero)
    elif numero < 100:
        carnet = "S0" + str(numero)
    else: 
        carnet = "S" + str(numero)
    estudiante["Nombre"] = nombre
    estudiante["Carnet"] = carnet
    lista.append(estudiante)

registrar_estudiante(lista)
print(lista)

#2 Escribe buscar_por_nombre(lista, nombre) que devuelva la tupla (carnet, nombre) si existe o None.
lista = []
def buscar_por_nombre(lista, nombre):
    for estudiante in lista:
        if estudiante[0].lower() == nombre.lower():
            return estudiante   # devuelve la tupla completa
    return None
    
#Probando
lista.append(("Camila", "S001"))
lista.append(("Michelle", "S002"))
lista.append(("Ruben", "S342"))

resultado = buscar_por_nombre(lista, nombre= "Camila")
if resultado:
    print("Encontrado:", resultado)
else:
        print("No existe")"""

#Escribe inscribir(lista_inscripciones, carnet, codigo_curso) que añada la tupla si no existe ya.
lista_inscripciones = []
def inscribir(lista_inscripciones, carnet, codigo): 
    for inscripción in lista_inscripciones: 
        if inscripción[0] == carnet and inscripción[1]== codigo:
            print(f"""El estudiante ya ha sido inscrito"   
| {inscripción}""")
            return 
        
    nueva_inscripción = (carnet, codigo)
    lista_inscripciones.append(nueva_inscripción)
    print(f"El estudiante ha sido inscrito con exito")
    
inscribir(lista_inscripciones, "C001", "MAT")
inscribir(lista_inscripciones, "C002", "SCI")
inscribir(lista_inscripciones, "C002", "SOC")
inscribir(lista_inscripciones, "C001", "MAT")

