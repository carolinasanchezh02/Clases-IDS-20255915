base_d_clientes = []
base_d_productos = []
base_d_pedidos = []
#Pedido = {}
cafeMenu =True
"""1.	Mostrar productos
2.	Agregar producto
3.	Registrar nuevo cliente
4.	Mostrar clientes
5.	Registrar pedido
6.	Mostrar pedidos del día
7.	Mostrar categorías disponibles
8.	Salir
"""

while cafeMenu:
    opción = input("""Elija la opción:  (1: Mostrar productos, 2: Agregar producto, 3: Registrar nuevo cliente, 
                   4: Mostrar clientes, 5: Registrar pedido, 6: Mostrar pedidos del día), 7: Mostrar categorías disponibles y 
                   8: Salir 
                   """)
    if opción == "1":
        print("Vamos a Mostrar los productos disponibles :D :")
        for n,c in base_d_productos.items():
            print(base_d_clientes)
    
    elif opción == "2":
        print("Vamos a agregar un producto")
        Producto= {}
        Producto["Nombre"]= input()
        Producto["Código"]= input()
        Producto["Categoría"]= input()
        Producto["Precio"]= float(input())
        base_d_productos.append(Producto)
        print(base_d_productos)
        print(Producto.items())
        
    elif opción == "3":
        print("Vamos a registrar un nuevo cliente :D :")
        Cliente= {}
        Cliente["Nombre"] = input().lower()
        Cliente["Código"] = input()
        Cliente["Correo"] = input().lower()
        Cliente["Teléfono"] = int(input())
        base_d_clientes.append(Cliente)
        print(base_d_clientes)
    
    elif opción == "4": 
        print("Vamos a mostrar a los clientes")
    elif opción == '8':
        cafeMenu = False 
print ("Usted ha salido del menú")
    
        

    
    
    
    
    

    
   