import modulo_datos
from modulo_funciones import registrar_estudiante


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
        print("lalalal")
    elif opcion == "3":
        print("lalala")
        
    elif opcion == '4':
        menu = False
    else:
        print("Opción inválida.")
print("Hemos salido del sistema.")   
