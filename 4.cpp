#include <iostream>
#include <cmath>

int main(){
{
// Суму S квадратів усіх елементів, що перевищують 10 по абсолютному
//значенню і їхню кількість К.
// Кожен елемент від -10 до 10 піносиш до квадрату і знаходиш їхню суму
// І кількість цифр від -10 до 10:

int n = 10;  // блок неявного вводу/выводу. - тіпа давайте повіримо шо є такі
//люди які це ПЧатают!

float sum = 0;  // Блок обробки данных - ініцілізація.

for (int i = -abs(n * 2), n = abs(n * 2); i < n; i++){
    sum += pow(i, 2);  // блок обробки данних.
}

cout << sum;  // блок вводу.выводу.
}

// або:
{
// Суму S квадратів усіх елементів, що перевищують 10 по абсолютному
//значенню і їхню кількість К.
// Cума елементів конкретного масиву:

int sum = 0;  // Блок обробки данных - констаннта.

int array = {
    {1, 2, 3},
    {3, 1, 2},
    {2, 3, 1}
};  // блок неявного вводу/выводу. - тіпа давайте повіримо шо є такі люди які це
//ПЧатают!

for (int j = 0; j < n; j++){
    for (int i = 0; i < n; i++){
        if (array[j][i] > 10){
            sum += array[j][i];  // блок обробки данних.
        }
    }
}
cout << sum;  // блок вводу/выводу.
}
}
