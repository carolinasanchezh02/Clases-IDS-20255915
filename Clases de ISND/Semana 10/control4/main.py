from libros import registrar_libro, mostrar_libros
from estudiantes import registrar_estudiante, mostrar_estudiantes
from prestamos import registrar_prestamo, mostrar_prestamos

lista_libros = []
lista_estudiantes = []
lista_prestamos = []

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar libro")
        print("2. Registrar estudiante")
        print("3. Registrar préstamo")
        print("4. Mostrar libros")
        print("5. Mostrar estudiantes")
        print("6. Mostrar préstamos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Vamos a registrar libro: ")
            registrar_libro(lista_libros)
        elif opcion == "2":
            print("Vamos a registrar estudiante: ")
            registrar_estudiante(lista_estudiantes)
        elif opcion == "3":
            print("Vamos a registrar prestamo: ")
            registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos)
        elif opcion == "4":
            print("Vamos a mostrar el libro: ")
            mostrar_libros(lista_libros)
        elif opcion == "5":
            print("Vamos a mostrar el carnet y datos del estudiante: ")
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == "6":
            print("Vamos a mostrar los prestamos: ")
            mostrar_prestamos(lista_prestamos)
        elif opcion == "7":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida.")

menu()
