#Este es un docstring de modulo. Vamos a crear varias funciones     <--- ejemplo de documentación

def funcion_saludar():
    """Es una función que va a saludar al usuario"""    #<- este es el mensaje que explica que hace la función
    nombre = input("Inserte su nombre")
    apellido = input("Inserte su apellido")
    print(f"Hola {nombre.capitalize()} {apellido.capitalize()}")
#vamos a llamar a la función
funcion_saludar() #tengo que si o sí llamarla para que s emuestre, si no solo existe.

def saludo_parametro(nombre, apellido): #lo que esta entre parentesis es el parametro
    """Es una función que saluda con parametro"""
    nombre_u = nombre
    apellido_u = apellido
    texto = f"El usuario se llama {nombre_u.title()} {apellido_u.title()}"
    print(texto)  
saludo_parametro("Maritza", "Geo") #lo que esta entre parentesis ya no es parametro, es argumento. fch

#AHora vamos a usar parametro y capturaremos la información con inputs. 
def capturar(nombre, edad):
    """Esta función captura los datos del usuario con inputs como parametros"""
    name = nombre
    age = edad
    text = f"Su usuario es {name.title()} y tiene {age.title()} años"
    print(text)
    
capturar(input("Ingrese su noombre completo: "), input("Ingrese su edad: "))