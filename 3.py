from math import exp, cos, tan

a = 3.7
p = 0.05  # Блок вичислень

i = float(input("i = "))
n = float(input("n = "))  # блок вводу.выводу

while (i < n):  # блок циклу
    x = a * exp(3)*i
    y = 2 * x * cos(i)  # блок вичислень

    if (x <= 1):  # блок розвилки - Так
        z = (1 + 2 * y*y) * cos(i)  # блок вичелсень

    else:  # блок розвилки - Ні
        z = pow(7.2 * x, 2) * tan(i)  # блок вичеслень

    i += p  # блок вичелсень

    print(z)  # блок вводу\виводу
