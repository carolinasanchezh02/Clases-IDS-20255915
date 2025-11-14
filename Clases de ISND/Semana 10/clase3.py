#kwargs es para parametro de diccionarios
#def registro_profesores(nombre, apellido, **materias):
    #"""Vamos a nombrar al docente y que materias imparte"""
    #print(f"El profesor {nombre}{apellido} imparte las materias: ")
    #for ciclo, materias in materias.items():
            #print(f"""- {ciclo}: {materias}""")

#Como le hago para llamar una funcion desde otro modulo
import modulo as fn
#import datos as dt
from datos import usuarios3 as u3 #para que de todo ese modulo solo me agarre esa lista en especifico

fn.registro_profesores(
                "Chema", 
                "Velasquez",
                Ciclo1 = ["Mate 1", "Física 1"],
                Ciclo2 = ["Mate 2, Física 2"],
                Ciclo3 = ["Precálculo", "Mecánica"])

fn.saludo_usuarios(u3)