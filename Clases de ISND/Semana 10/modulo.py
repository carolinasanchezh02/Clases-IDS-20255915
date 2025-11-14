#Este modulo contendra las funciones
def ordenar_pizza(size, *ingrediente): 
    """"Vamos a imprimir la orden"""
    print(f"Usted ha ordenado una pizza {size} de: ")
    for i in ingrediente: 
        print(f"""- {i}""")

def registro_profesores(nombre, apellido, **materias):
    """Vamos a nombrar al docente y que materias imparte"""
    print(f"El profesor {nombre}{apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
            print(f"""- {ciclo}: {materias}""")

def saludo_usuarios(nombres):
    """Saludara a los usuarios en la lista"""
    for nombre in nombres:
            print(f"Hola, {nombre.capitalize()}")