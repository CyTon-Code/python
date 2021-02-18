from math import exp, cos, tan

x, y, z = 0,0,0
i = 0.30
n = 0.60
p = 0.05
a = 0

while i < n:
    x = a * exp(3*i)
    y = 2*x * cos(i)

    if x <= 1:
        z = (1 + 2 * y**2) * cos(i)

    else:
        z = (7.2 * x)** 2 * tag(i)

    i += p

    print(z)
