from math import exp, cos, tan

# x = 0
# y = 0
# z = 0
a = 3.7

i = float(input("i = "))
n = float(input("n = "))
p = 0.05

while (i < n):
    x = a * exp(3)*i
    y = 2 * x * cos(i)

    if (x <= 1):
        z = (1 + 2 * y*y) * cos(i)

    else:
        z = pow(7.2 * x, 2) * tan(i)

    i += p

    print(z)
