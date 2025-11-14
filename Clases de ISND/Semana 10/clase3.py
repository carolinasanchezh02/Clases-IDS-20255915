#kwargs es para parametro de diccionarios
def registro_profesores(nombre, apellido, **materias):
    """Vamos a nombrar al docente y que materias imparte"""
    print(f"El profesor {nombre}{apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
            print(f"""- {ciclo}: {materias}""")
            
registro_profesores("Alvin", 
                    "POrTillO", 
                    Ciclo1 = ["Intro a ISND", "lalala"], 
                    Ciclo2 = ["Proga orientad a aobjeto", "dd"], 
                    Ciclo3 = ["Probabilidad", "sdad"])

