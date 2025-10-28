"""
#1 
numero = int(input())
if numero > 0: 
    print("Positivo")
else:
    print("Negativo")

#2
s = int(input())
if s%2 == 0:
    print(s+2)
else: 
    print(s+1)
if s%2 == 0: 
    print(s-1)
else: 
     print(s-2)

#3
c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
c5 = float(input())
c6 = float(input())
promedio = (c1 + c2 + c3 + c4 + c5 + c6)/6

if promedio > 9.5: 
    print("Gana Premio :)")
else: 
    print("No Gana Premio :(")"""
    
    
###4  LO TENGO MALO NO SEEEEE-> RTE
"""N = int(input())
conteo_n1 = 0
conteo_n2 = 0
for i in range(N):
    numero = int(input())
    if numero == 7: 
        conteo_n1 += 1
    elif numero == 5: 
        conteo_n2 += 1
print (conteo_n1, conteo_n2)

###5
N = int(input())
Pa, Pb, Pc = map(int, input().split())

for i in range(N): 
    combo = input().upper()
    comboA= combo.count("A")*Pa
    comboB = combo.count("B")*Pb
    comboC = combo.count("C")*Pc  
    print(comboA+comboB+comboC)
    
###7
N = int(input())
lista = []
for i in range(N):
    nombres = input().lower()
    lista.append(nombres)

for nombre in lista:
    cantL = len(nombre)
    if cantL <= 6: 
        print("No vale la pena")
    elif cantL >= 8: 
        print("Si aguanto otro desarrollo de personaje")
    else: 
        print("Dios no creo aguantar esta vez")"""    
    
    

###8 
"""x = int(input())
y = int(input())
print(max(x, y))

mi solución: 
if x>y: 
    print(x)
elif x== y: 
    print(x)
else: 
    print(y)
    
segun gepete: 
x, y = map(int, input().split())
if x > y:
    print(x)
else:
    print(y)

##9
estado = input()
if estado == "conectado":
    print("Ola Ivan")
else: 
    print("Ol...")
    
##8 
A = int(input())
ingresos = 0
for i in range(A):
    edades = int(input())
    if edades >= 15:
        ingresos += 1
print(ingresos)

###10
N = int(input())
for i in range(N):
    P = int(input())
    if P >= 3:
        print("Ok")
    else:
        print("No")"""        
        
    
