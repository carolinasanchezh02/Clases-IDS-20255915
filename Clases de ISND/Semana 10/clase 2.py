#Trabajando definicion de funciones y usando listas
def saludo_usuarios(nombres):
    """Saludara a los usuarios en la lista"""
    for nombre in nombres:
            print(f"Hola, {nombre.capitalize()}")
            
usuarios = ["Fer", "MOI", "LuIs"]
#saludo_usuarios(usuarios)

#Quiero atender pedidos con varios ingredientes   parametro args -< una cantidad variable de argumentos
def ordenar_pizza(size, *ingrediente): #ahora va recibir varios ingredientes como si fuera uan lista, le estoy indicando que trate ese parametro como una lista. 
    #Normalmente los parametros tipo args denben dejarse al final
    """"Vamos a imprimir la orden"""
    print(f"Usted ha ordenado una pizza {size.capitalice()} de: ")
    for i in ingrediente: 
        print(f"""- {i}""")
ordenar_pizza("gRANDE", "queso", "tocino", "chile", "piña")        
    
    