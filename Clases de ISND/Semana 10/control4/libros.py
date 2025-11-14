libros = []
contador = 0

"""if contador < 10:
    codigo = "L00" + str(contador)
elif contador < 100:
    codigo = "L0" + str(contador)
else:
    codigo = "L" + str(contador)"""

def registrar_libro():
    r_libro = True
    print("Vamos a registrar un libro: ")
    while r_libro:
        if len(libros) < 10:
            contador += 1
            codigo = "L00" + str(contador)
        elif len(libros) < 100:
            codigo = "L0" + str(contador)
        else:
            codigo = "L" + str(contador)
        print("Vamos a registrar un libro: ")
        Libro= {}
        Libro["Nombre"]= input("Ingrese el nombre del libro: ")
        Libro["Autor"]= input("Ingrese el autor del libro: ")
        Libro["Codigo"] = codigo
        Libro["Disponible"]= True
        libros.append(Libro)
        print(libros)
        break
    