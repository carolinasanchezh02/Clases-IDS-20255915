def dui_validacion(dui):
    contador = 0
    if len(dui) == 10:
        contador +=1
    if dui.count("-") == 1:
        contador += 1
    if dui[-1] != "-" and dui[-2]== "-":
        contador += 1
    print(f"Cumple {contador} condiciones")
dui_validacion("123478-9")