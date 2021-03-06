from math import exp, cos, tan

x, y, z = 0, 0, 0
i = 0.30
n = 0.60
p = 0.05
a = 0  # block исчислений - ініціалізація.

while i < n:  # block цикла.
    x = a * exp(3 * i)
    y = 2 * x * cos(i)  # блок исчислений

    if x <= 1:  # Розвилка Так
        z = (1 + 2 * y ** 2) * cos(i)

    else:  # Розвилка Ні
        z = (7.2 * x) ** 2 * tan(i)

    i += p  # block исчислений.

    print(z)  # блок ввода/вывода
