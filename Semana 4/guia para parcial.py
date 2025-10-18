"""A= int(input())
B= int(input())
C= int(input())
D= int(input())
print((A*B)-(C*D))"""

"""dato1 = float(input())
dato2 = float(input())
dato3 = float(input())
dato4 = float(input())
dato5 = float(input())
dato6 = float(input())
lista = [dato1, dato2, dato3, dato4, dato5, dato6]
max = max(lista)
min = min(lista)
print(f"Maximo: {max: .2f}")
print(f"Minimo: {min: .2f}")
print(f"Diferencia: {max-min: .2f}")
print(f"Suma: {sum(lista): .2f}")
print(f"Promedio: {((sum(lista))/6): .2f}")"""

"""num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = float(input())
num7 = float(input())
num8 = float(input())
num9 = float(input())
num10 = float(input())
pta1 = num1*num6
pta2 = num2*num7
pta3 = num3*num8
pta4 = num4*num9
pta5 = num5*num10
print(int(pta1+pta2+pta3+pta4+pta5))"""

nombre = input()
apellido = input()
nick = (nombre[0:5] + apellido[0]).lower()
pin = ((len(nombre) * 1000)+ len(apellido))%10000
print(f"""
      Nick: {nick}
      Pin: {pin}
      ID: C3-{nick}-{pin}
      """)