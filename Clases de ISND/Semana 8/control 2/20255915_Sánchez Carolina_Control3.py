"""Nombre: Carolina Michelle Sánchez Herrera 
    CARNET: 20255915
    'Por mi honor y ante mis compañeros, me comprometo a no copiar, para que este examen refleje mi verdadero nivel de conocimientos"""


##1 
agente = "encargado"
platillos = []
precios = []
app = True
name_agente = input("Ingrese el nombre del agente: ")
##2
while name_agente != agente: 
    print(f"Agente no registrado")
    name_agente = input("Favor ingrese el nombre del agente:")
#3
while app: 
    opción = input("Eliga la acción que desea realizar: (1: Creación de platillos, 2: Consulta de platillos y precios, 3: Colocar un pedido, 4: Salir)")
    ###4
    if opción == "1":
        plato = input("Ingrese el nombre del platillo a crear: ").lower()
        precio = float(input("Ingrese el precio del platillo a crear: "))
        platillos.append(plato)
        precios.append(precio)
    ###5
    elif opción == "2":
        if platillos == []: 
            print("Actualmente no hay platillos ingresados")
        else:
            for platoo in platillos: 
                cual = platillos.index(plato)
                print(f"{platillos[cual]}: ${precios[cual]}")
    ###6                
    elif opción == "3":
        elección = input("Indique el nombre del platillo para su orden: ")
        if elección in platillos:
            selección = platillos.index(elección.lower())
            print(f"Usted ha elegido {platillos[selección]} con un precio de ${precios[selección]}")
        else: 
            print("El nombre del platillo ingresado no existe")
    ###7
    elif opción == "4":
        app = False
print("Usted ha salido de la aplicación. ")