from math import log, cos

x = float(input("x = "))
c = float(input("c = "))
a = float(input("a = "))  # блок вводу/виводу

с = log(c)
a = a * c + x**2
b = x**2 + c
y = (((a*x)** 3)+b)/cos(x)** 3  # блок вичеслень.

print(y)  # блок вводу/виводу
