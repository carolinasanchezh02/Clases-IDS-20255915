from modulo_datos import Cursos_Disponibles
from modulo_datos import lista_estudiantes
from modulo_datos import lista_inscripciones


def registrar_estudiante(lista_estudiantes):
    estudiante = {}

    carnet = input("Ingrese su carnet: ")
    if len(carnet) < 6 or len(carnet) > 10:
        print("Carnet inválido")
        return

    # Validación de nombre y apellido
    while True:
        nombre = input("Ingrese su nombre: ").lower()
        apellido = input("Ingrese su apellido: ").lower()

        if len(nombre) >= 2 and len(apellido) >= 2:
            break
        else:
            print("El nombre y apellido deben tener al menos 2 caracteres.")

    # Guardamos los datos
    estudiante["Carnet"] = carnet
    estudiante["Nombre"] = nombre.capitalize()
    estudiante["Apellido"] = apellido.capitalize()

    lista_estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.")
  
  
def inscribir_en_curso(lista_estudiantes, Cursos_Disponibles, lista_inscripciones):
    while True:
        op = input("\n 'inscribir' para inscribir / 'salir' para regresar: ").lower()

        if op == 'salir':
            break

        elif op == 'inscribir':
            solicitud_carnet = input("Ingrese su carnet: ")
            existe = False
            for est in lista_estudiantes:
                if est["Carnet"] == solicitud_carnet:
                    existe = True
                    break

            if not existe:
                print("El carnet NO existe. Intente nuevamente.")
                continue   # vuelve al menú de inscripción

            #Mostrar cursos disponibles
            print("\nCursos disponibles:")
            for c in Cursos_Disponibles:
                print(f"- {c}")
            while True:
                codigo = input("Ingrese el código del curso: ").upper()
                if codigo not in Cursos_Disponibles:
                    print("Ese curso no existe. Ingrese uno válido.")
                    continue
                break
            
            ya_inscrito = False
            for ins in lista_inscripciones:
                if ins[0] == solicitud_carnet and ins[1] == codigo:
                    ya_inscrito = True
                    break
            if ya_inscrito:
                print("Ya estás inscrito en este curso.")
                continue
            inscripcion = (solicitud_carnet, codigo)
            lista_inscripciones.append(inscripcion)
            print("Inscripción realizada con éxito.")
        else:
            print("Opción no válida, intente nuevamente.")
            
        
            
def generar_reporte(lista_inscripciones, lista_estudiantes):
    if len(lista_inscripciones) == 0: 
        print("No hay inscripciones hechas")
        return
    
    Opciones = {
        "1" : "PY",
        "2" : "JS",
        "3" : "BD",
        "4" : "SE",
        "5": "SIN"}

    
    print("\n--- GENERAR REPORTE ---")
    print("""
          1. PY 
          2. JS 
          3. BD
          4. SE
          5. SIN (Estudiantes sin inscripción) """)
    selección = input("Seleccione una de las opciones (1-5): ")
    

    if Opciones[selección] == "SIN":
        carnets_inscritos = []
        for ins in lista_inscripciones:
            if ins[0] not in carnets_inscritos:
                carnets_inscritos.append(ins[0])
        print("\nEstudiantes sin inscripción:")
        encontrado = False
        for est in lista_estudiantes:
            if est["Carnet"] not in carnets_inscritos:
                print(f"- {est['Nombre']} {est['Apellido']} (Carnet: {est['Carnet']})")
                encontrado = True
        if not encontrado:
            print("Todos los estudiantes tienen al menos una inscripción.")
        return
    codigo_curso = Opciones[selección]
    print(f"""Carnets inscritos en el curso {codigo_curso} - {Cursos_Disponibles.get(codigo_curso, '')}:""")

    encontrados = []
    for ins in lista_inscripciones:
        if ins[1] == codigo_curso:
            encontrados.append(ins[0])

    if len(encontrados) == 0:
        print("Nadie está inscrito en este curso.")
    else:
        for c in encontrados:
            print(f"- {c}")
    return
    
    
    


