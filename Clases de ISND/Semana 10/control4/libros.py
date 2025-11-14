libros = []
registrar_libro = True
contador = 1

while registrar_libro:
    opción = input("""Elija la opción:  (1: Registrar libro, 2: Registrar estudiante, 3: Registrar préstamo, 
                   4: Mosntrar libros, 5: Mostrar estudiantes, 6: Mostrar prestamos, 7: Salir) 
                   """)
    
    
    if opción == "1":
        codigo = f"L00{contador}"
        contador += 1
        print("Vamos a registrar un libro: ")
        Libro= {}
        Libro["Nombre"]= input("Ingrese el nombre del libro: ")
        Libro["Autor"]= input("Ingrese el autor del libro: ")
        Libro["Código"] = codigo 
        Libro["Disponible"]= True
        libros.append(Libro)
        print(libros)
        
    