libros = []
ejercicio = True

while ejercicio: 
    accion = input("""¿Qué hacemos?
    1: Agregar libro al registro
    2: Buscar autor y sus obras
    3: Consultar disponibilidad
    4: Buscar y eliminar dupicados
    8: Salir 
    """)
    if accion == '1':
        libro = {}
        
        numero = len(libros) + 1
        if numero < 10:
            codigo = "L00" + str(numero)
        elif numero < 100:
            codigo = "L0" + str(numero)
        else:
            codigo = "L" + str(numero)
            
        libro["Codigo"] = codigo
        libro["Título"] = input("Título del libro: ").lower()
        libro["Autor"] = input("Autor del libro: ").lower()
        #libro["Código"] = codigo
        libro["Disponibilidad"] = True
        libros.append(libro)
    elif accion == '2': 
        busqueda = input("¿Qué autor desea buscar?").lower()
        estado = False
        for b in libros: 
            if b["Autor"] == busqueda:
                print(f"""{b['Título'].title()} (Código: {b['Codigo']})""")
                estado = True
        if not estado: 
            print("Autor no registrado")
    elif accion == '3':
        print()
    elif accion == '4':
        objetivo = input("Ingrese el título del libro que desea consultar: ").lower()
        existencia = False
        for l in libros: 
            if l['Título'] == objetivo:
                existencia = True
                break
        if existencia: 
            print("Este libro ya se encuenta en existencias")
            #dec = input("¿desea eliminarlo? si/no: ").lower()
            #if dec == 'si' or 'sí': 
        else: 
            print("El libro es el único")
    elif accion == '8': 
        ejercicio = False
        
print("Byebye")
    
