import math  # log, cos

x = float(input("x = "))
c = log(float(input("c = ")))
a = float(input("a = ")) * c + x**2
b = x**2 + c

y = (((a*x)** 3)+b)/cos(x)** 3

print(y)

