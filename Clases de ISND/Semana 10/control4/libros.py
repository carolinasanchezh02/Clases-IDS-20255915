#para ingresar libros y sus datos
def registrar_libro(lista_libros):
    """Para registrar los datos de un libro"""
    Libro = {}
    numero = len(lista_libros) + 1
    if numero < 10:
        codigo = "L00" + str(numero)
    elif numero < 100:
        codigo = "L0" + str(numero)
    else:
        codigo = "L" + str(numero)
    Libro["Codigo"] = codigo
    Libro["Nombre"] = input("Ingrese el nombre del libro: ")
    Libro["Autor"] = input("Ingrese el autor del libro: ")
    Libro["Disponible"] = True

    lista_libros.append(Libro)
    print(f"El codigo de su libro es {Libro["Codigo"]}")


#para mostrar los libros
def mostrar_libros(lista_libros):
    """Para mostrar los libros registrados"""
    for buk in lista_libros:
        print(buk)