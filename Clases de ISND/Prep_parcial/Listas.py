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
    7: Consultar
    """)
    if accion == '1': 
        print("Hola, vamos a agregar tus artistas favoritos a una lista :D")
        artista = input("Inserte el nombre de su artista o banda preferido: ").lower()
        bandas.append(artista.title())
        print("Hemos agregado tu artista exitosamente")
    elif accion == '2': 
        print("""Estos son tus artistas y bandas preferidas: """)
        print(bandas)
    elif accion == '3':
        print("Vamos a modificar la lista")
        amodificar = int(input("Ingrese la posición del objeto a modificar: "))
        bandas[amodificar-1] = input("Ingrese lo que desea modificar: ").lower()
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
    elif accion == '7':
        AC = input("¿Qué quieres hacer? N: Identificar el objeto en una posición en específico / E: Saber si X esta en la lista").upper()
        if AC == 'N': 
            pos = int(input("Inserte el número de la posición que le interesa: "))
            busqueda = bandas[pos-1]
            #resultado = bandas.index(pos-1)
            print (f"Su artista/ banda es: {busqueda}")
        else: 
            duda = input("Inserte el nombre del artista/Banda que busca: ").title()
            if duda in bandas:
                consultar = bandas.index(duda)
                print(f"Su artista, {duda}, sí esta en la lista en la posición {consultar+1}")
            else: 
                print("Su artista no esta en la lista.")
                conf = input("¿Desea agregarlo? Si/No").lower()
                if conf == 'si' or 'sí': 
                    bandas.append(duda)
                    print("Su artista ha sido agregado")
                    print(bandas)
                else: 
                    print("Regresaremos al menú")
                    continue
print ("Hemos finalizado el listado, haz salido del sistema >:D")