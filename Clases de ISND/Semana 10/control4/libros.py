contador = 0
print("Vamos a registrar un libro: ")
def registrar_libro(lista_libros):
    r_libro = True
    while r_libro:
        if len(lista_libros) < 10:
            contador += 1
            codigo = "L00" + str(contador)
            Libro["Codigo"] = codigo
        elif len(lista_libros) < 100:
            codigo = "L0" + str(contador)
            Libro["Codigo"] = codigo
        else:
            codigo = "L" + str(contador)
            Libro["Codigo"] = codigo
        Libro= {}
        Libro["Nombre"]= input("Ingrese el nombre del libro: ")
        Libro["Autor"]= input("Ingrese el autor del libro: ")
        Libro["Disponible"]= True
        lista_libros.append(Libro)
        break
registrar_libro()   