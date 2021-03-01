from math import log, cos

x = float(input("x = "))
c = float(input("c = "))
a = float(input("a = "))  # блок ввода/вывода

c = log(c)
a = a * c + x ** 2
b = x ** 2 + c
y = (((a * x) ** 3) + b) / cos(x) ** 3  # блок исчислений.

print(y)  # блок ввода/вывода
