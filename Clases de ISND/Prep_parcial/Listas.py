bandas = []
si = True

while si: 
    print("Bienvenide amigue")
    accion = input("""¿Qué quieres hacer? 
    -------------------------------------------------------------------------------
    1: Agregar un artista
    2: Mostrar lista de artistas
    3: Modificar lista 
    4: Eliminar elemento
    5: Salir
    6: Enunciar
    """)
    if accion == '1': 
        print("Hola, vamos a agregar tus artistas favoritos a una lista :D")
        artista = input("Inserte el nombre de su artista o banda preferido: ")
        uno = bandas.append(artista)
        print("Hemos agregado tu artista exitosamente")
    elif accion == '2': 
        print("""Estos son tus artistas y bandas preferidas: """)
        print(f"""{bandas}""")
    elif accion == '3':
        print("Vamos a modificar la lista")
        amodificar = int(input("Ingrese la posición del objeto a modificar: "))
        bandas[amodificar-1] = input("Ingrese lo que desea modificar: ")
    elif accion == '4': 
        print("Vamos a eliminar un elemento de su lista")
        borrar = int(input("Ingrese la posición del objeto a eliminar"))
        eliminado = bandas.pop(borrar-1)
        print(f"El objeto que usted ha eliminado de la lista ha sido {eliminado}")
    elif accion == '5': 
        si = False
    elif accion == '6':
        print("Vamos a recorrer su lista para que haga enunciados afirmativos")
        for n in bandas: 
            print(f"""
                  Me gusta mucho: {n}""") 
print ("Hemos finalizado el listado, haz salido del sistema >:D")