# Vamos a crear un diccionario
"""mi_gato= {"Pelusa", 3, "simpatica"} #[Nombre, edad, caracteristica]
print(len(mi_gato))
print(type(mi_gato)) #Da "set" porque no hay valores definidos.


#SET
mi_gato = {
"nombre": "pelusa", 
"edad": 3, 
"personalidad": "simpatico"
}
print(type(mi_gato))
print(len(mi_gato))
 #Da "dict" porque se le dan valores ya definidos para su comprensión



pame_cat= {
    "personalidad" : "simpatico" ,"nombre" : "pelusa", 
"edad" : 3
}

copia = mi_gato== pame_cat
print(copia)"""

birthdays= {"Alice" : "Apr 1",
            "Bob": "Dec 12",
            "Carol" : "Mar 4"
            }

birthdays["Carol"]= "Apr 21" 
birthdays["Fer"] = "Mar 3" #No usamos .append, ya que es un organigrama, para agregar un nuevo valor.
del birthdays["Bob"] #"del" al inicio para borrar un valor.
print(birthdays)

for persona, fecha in birthdays.items():
    print(f"El cumpleaños de {persona} es en {fecha}")
    
"""semana= {}
semana["uno"] = "lunes"
semana["dos"] = "martes"
semana["tres"] = "miercoles"
semana["cuatro"] = "jueves"
semana["cinco"] = "viernes"
print(semana)"""

"""for k,v in semana.items():#.values es un metodo para referirnos a los valores que tiene una "variable"  (*clave: VALOR(value))
    '"""'print (k)'"""
    print (f"El día {k} de la semana es {v})"""
    
    