nombre = "Carolina"
palabra = "reconocer"
otra_palabra = "palabra"

print(nombre)
print(nombre[2])
print(nombre[2:])
print(len(palabra))
print(palabra[4:9]) #desde quinto caracter "n" hasta la "c". Es decir, que imprima "NOCER"
print(palabra[1::2])#para hacer saltos entre caracteres. Inicia en el que digo, y cuanto irá sañtando <- este e spara que me imprima las vocales
print(palabra[0::2])
#len es para que me diga cuaal es el length de lo que esta dentro de la variable

#Si quito los pares de numero sy dejo los puntos, me imprimiria todo
print(palabra[::-2]) #para que vaya al reves 
"""print(nombre[2]) <- para que me imprima solo la letra que esta en esa posición
print(nombre[2:]) para que me imprima todas las letras si no llego a conocer cuanto es en lo ultimo (el limite)
Reconocer tiene 9 caracteres porque su indice es 8, los caracteres se leen desde la posicion0 a su final pero esta o cuenta cuando se trata de length

"""
#palitro = una palabra que sea al reves y derecho de manera igual
print(otra_palabra[::-1])# <- para que me lo diga al reves

#OJO LOS ESPACIOS ENTRE ORACIONES CUANTAN COMO POSICIONES
"""Para saber si es palitro utilizo lo siguiente"""
palabro = "sorbete"
print(palabro==palabro[::-1])   #literal estoy comparando si la palabra og es igual a la escrita de forma inversa  <- esto me dira si se cumple o no con TRUE or FALSE



"""numero = 255
print(len(numero)) <- ESTO NO SE VA PODER 
#PQ len no podria usarala con un int pq no se les puede identificar una extensión específica 

funcionaria si hago 255 como texto"""
numero = "255"
print(len(numero))

"""METODOS: Darles indicaciones al objeto para que haga algo. 
LLevan parentesis pq son funciones aplicadas a objetos"""
mi_palabra = "jocote"
print(mi_palabra)

mayuscula = mi_palabra.upper()                #ORIGEN.DEPENDIENTE (propiedades y metodos)
print(mayuscula)


