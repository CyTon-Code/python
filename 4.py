# Суму S квадратів усіх елементів, що перевищують 10 по абсолютному
#значенню і їхню кількість К.
# Кожен елемент від -10 до 10 піносиш до квадрату і знаходиш їхню суму
# І кількість цифр від -10 до 10:

n = 10  # блок неявного вводу/выводу. - тіпа давайте повіримо шо є такі
#люди які це ПЧатают!

sum = 0  # Блок обробки данных - ініцілізація.

for i in range(-abs(n * 2),abs(n * 2)):
    sum += i ** 2  # блок обробки данних.

print(sum)  # блок вводу.выводу.


# або:

# Суму S квадратів усіх елементів, що перевищують 10 по абсолютному
#значенню і їхню кількість К.
# Cума елементів конкретного масиву:

sum = 0  # Блок обробки данных - констаннта.

array = [
[1, 2, 3],
[3, 1, 2],
[2, 3, 1]
]  # блок неявного вводу/выводу. - тіпа давайте повіримо шо є такі люди які це
#ПЧатают!

for j in array:
    for i in j:
        if i > 10:
            sum += i  # блок обробки данних.

print(sum)  # блок вводу/выводу.
