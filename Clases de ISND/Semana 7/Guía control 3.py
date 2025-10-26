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
    print("No Gana Premio :(")

## 6 me quede aca, lol
N = []
N.append(input())
condi1 = len(N[1])

### 8 en este no se q caso estoy omitiendo pero me da RTE
x = int(input())
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
    print("Ol...")"""
    
