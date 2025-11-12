def dui_validacion(dui):
    contador = 0
    if len(dui) == 10:
        contador +=1
    if dui.count("-") == 1:
        contador += 1
