number = int(input('Введите число: '))
first_number = number // 10
number_1 = first_number // 10
number_2 = first_number % 10
number_3 = number % 10
print(
    f'Сумма цифр = {number_1 + number_2 + number_3}', 
    f'Произведение цифр = {number_1 * number_2 * number_3}', 
    sep = '\n'
)

Ввод:
Введите число: 847
Вывод:
Сумма цифр = 19
Произведение цифр = 224