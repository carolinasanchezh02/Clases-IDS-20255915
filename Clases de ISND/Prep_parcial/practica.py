colores = {
    "primario": "rojo",
    "secundario": "verde",
    "bandera": "rojo",
    "extra": "amarillo",
    "decoracion": "verde"
}

repetidos = []
colors = list(colores.values())
for n in colors: 
    if colors.count(n)>1 and n not in repetidos: 
        repetidos.append(n)
print(f"Los colores repetidos son: {repetidos}") 

for key in colores: 
    for keys in colores: 
        if key != keys:
            if colores[key] == colores[keys]:
                print(f"{key} - {keys}")
