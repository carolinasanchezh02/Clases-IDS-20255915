"""nota = float(input("Digite la nota: "))
if nota >8: 
    print("Excelente")
elif nota > 6:
    print("Muy bien")
elif nota > 4: 
    print("Regular")
else: 
    print("Mal")""" 
    
#If anidado
"""Supongamos que tengo dos tipos de producto: local e internacional
- No es necesario declara dos variables. 
- Se puede discriminar con el if

"""
monto = float(input("Ingrese el monto dle producto: "))
tipo = input("Tipo (local/internacional): ")
if tipo.lower() == "local": 
    if monto > 100: 
        print("7%")
    elif monto > 75: 
        print("5%")
    else: 
        print("0%")
else:                               #OJO: pYTHON FUNCIONA CON INDENTACIÓN, oJITO CON LOS LAS TABULACIONES
    if monto > 100: 
        print("12%")
    elif monto > 75: 
        print("9%")
    else: 
        print("0%")

#Solucion de ALvin
monto = float(input("Ingrese el monto de su producto: "))
tipo = input("Tipo (local/internacional): ")
impuesto = 0
if tipo.lower() == "local": 
    if monto > 100: 
        impuesto == 0.07
    else: 
        if monto > 75: 
            impuesto == 0.05
        else: 
            impuesto == 0
elif tipo.lower() == "internacional": 
    if monto > 100: 
        impuesto == 0.12
    elif monto > 75: 
        impuesto == 0.09
    else: 
        impuesto == 0
else: 
    print("Ese tipo no existe vv, checa eso porfa")
print(f"El tipo {tipo} con monto {monto: ,.2f} paga un impuesto de {monto*impuesto: ,.2f}")
# Una buena práctica es trabajar con mis variables y de jar los print al final porque puede paasar que el cliente me 
# cambie mis requerimientos al final de todo y así me evito ir linea con linea cambiando el print. 