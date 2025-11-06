#Este es un docstring de modulo. Vamos a crear varias funciones     <--- ejemplo de documentación

def funcion_saludar():
#explicación de la función
    """Es una función que va a saludar al usuario"""
    nombre = input("Inserte su nombre")
    apellido = input("Inserte su apellido")
    print(f"Hola {nombre.title()} {apellido.title()}")
funcion_saludar() #tengo que si o sí llamarla para que s emuestre, si no solo existe.

def saludo_parametro(nombre, apellido): #lo que esta entre parentesis es el parametro
    """Es una función que saluda con parametro"""
    
    
    print(f"Hola {nombre} {apellido}") #aqui ya ouse a chambear el parametro. 
    
saludo_parametro("Moi", "G") #lo que esta entre parentesis ya no es parametro, es argumento. fch