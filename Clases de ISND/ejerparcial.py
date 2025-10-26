"""fecha = input()
print(f"{fecha[6:10]}{fecha[2:6]}{fecha[0:3]}")"""

platos = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")
posi1 = int(input())
posi2 = int(input())

print(f"El pedido de Alvin es: {platos[posi1-1]} con {complementos[posi2-1]}")