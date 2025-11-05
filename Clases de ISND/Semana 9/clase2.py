thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""Podemos hacer for para dos listas distintas, 
enumerate()"""

surname = ['Rivest', 'Shamir', 'Adleman']
for position, surnames in enumerate(surname, start = 1):    #enumarate es para cuando necesitás tanto el índice como el valor de una lista
    #el start lo que hace es que en lugar d emostrarme el indice inicial en 0, como lo hace por q si, lo haria forazando q el 0 sea 1.
    print(position, surnames)

#position es un numero arbitable que yo construyo. 

#zip()
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
for person, age in zip(people, ages): 
    print(person, age)
    
#las 'variables2 despues del for son arbitrarias, yo las asigno para designar los elementos  amostrar. Toma muchas listas y hacer una iteración para cada una en el primer iterador de cad alista
#Las pone en paralelo.. -> Toma el largo del menor de las listas (largo de elementos dentro de la lista. SI las demas listas tienen mas elementos, las ignora)