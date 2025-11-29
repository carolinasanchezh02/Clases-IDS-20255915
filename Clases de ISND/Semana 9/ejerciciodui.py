def dui_validacion(dui):
    contador = 0
    if len(dui) == 10:
        contador +=1
    if dui.count("-") == 1:
        contador += 1
    if dui[-2] == "-":
        contador += 1
    parte1 = dui[:8]
    parte2 = dui[-1]
    if parte1.isdigit() and parte2.isdigit(): 
        contador +=1
    print(f"Cumple {contador} condiciones")
dui_validacion("07525558-1")