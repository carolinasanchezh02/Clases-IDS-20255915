from modulo_datos import lista_estudiantes, lista_inscripciones, Cursos_Disponibles
from modulo_funciones import registrar_estudiante, inscribir_en_curso, generar_reporte


menu = True

while menu: 
    opcion = input("""¿Qué desea hacer?
1. Registrar estudiante
2. Inscribir en curso
3. Generar reportes
4. Salir
""")
    if opcion == '1': 
        registrar_estudiante(lista_estudiantes)
    elif opcion == "2":
        inscribir_en_curso(lista_estudiantes, Cursos_Disponibles, lista_inscripciones)
    elif opcion == "3":
        generar_reporte(lista_inscripciones, lista_estudiantes)
    elif opcion == '4':
        menu = False
    else:
        print("Opción inválida.")
print("Hemos salido del sistema.")   
