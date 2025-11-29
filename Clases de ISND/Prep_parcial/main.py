from modulo_datos import lista_estudiantes, lista_inscripciones, cursos_disponibles
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
        registrar_estudiante()
    elif opcion == "2":
        inscribir_en_curso()
    elif opcion == "3":
        generar_reporte()
    elif opcion == '4':
        menu = False
    else:
        print("Opción inválida.")
print("Hemos salido del sistema.")   
