#para registrar un prestamso
from libros import registrar_libro, mostrar_libros
from estudiantes import registrar_estudiante, mostrar_estudiantes

def buscar_estudiante(lista_estudiantes, carnet):
    for estudiante in lista_estudiantes:
        if estudiante["Código"] == carnet:
            return estudiante
    return None

def buscar_libro(lista_libros, codigo):
    for libro in lista_libros:
        if libro["Codigo"] == codigo:
            return libro
    return None

def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    print("""Registrar Préstamo""")
    carnet = input("Ingrese el carnet del estudiante: ")
    estudiante = buscar_estudiante(lista_estudiantes, carnet)
    if estudiante is None:
        print("carnet no encontrado.")
        return
    codigo = input("Ingrese el código del libro a solicitar: ")
    
    libro = buscar_libro(lista_libros, codigo)
    if libro is None:
        print("libro no encontrado.")
        return
    if not libro["Disponible"]:
        print("El libro NO está disponible")
        return
    
    fecha = input("Ingrese la fecha del préstamo (e.g.: 2025-11-14): ")

    prestamo = {
        "Estudiante": carnet,
        "Libro": codigo,
        "Fecha": fecha
    }
    lista_prestamos.append(prestamo)

    libro["Disponible"] = False
    print("Préstamo registrado con exito")