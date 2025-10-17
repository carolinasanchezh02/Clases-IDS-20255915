###1
"""correo = input()
condición1 = correo.count('@')== 1
condición2 = correo.index('@')>=3
arroba = correo.index('@')
condición2_1 = (len(correo)-arroba) > 3
condición3 = correo.count('.')>= 1
condición4 = correo.count(' ')== 0
condición5 = correo[0] != '.'  # "!=" es no sea igual
condición5_1 = correo[-1] != '.'

#me dira true si TODAS se cumplen 
print(condición1 and condición2 and condición2_1 and condición3 and condición4 and condición5 and condición5_1)

###2
cadena = input()
print(cadena.lower().count("z")) #en caso de que en la cadena hayan mayusculas y minuusculkas y me cuente todas sin perder datos
#concatenee funciones arribaaa"""

### 3
x = int(input())
A = input()
B = input()
parte1 = A[:x]
parte2 = B[-x:] #-x para denotar que empiece desde el final

"""Tengo a lapiz como mi valor de variable
 entonces si quiero que me de los primeros tres caracteres pero al revez, osea pal, 
 es variable[:3:][::-1] <- primero me discrima que aagarra desde el inicio hasta el caracter con poiscion 3
 y despues me los da al reves"""

print(parte1+parte2)