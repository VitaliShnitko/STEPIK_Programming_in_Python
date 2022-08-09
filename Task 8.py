# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
# после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

number_1 = float(input())
number_2 = float(input())
sign = input()
if sign == '+':
    print(number_1 + number_2)
elif sign == '-':
    print(number_1 - number_2)
elif sign == '/':
    if number_2 == 0:
        print('Деление на 0!')
    else:
        print(number_1 / number_2)
elif sign == '*':
    print(number_1 * number_2)
elif sign == 'mod':
    if number_2 != 0:
        print(number_1 % number_2)
    else:
        print('Деление на 0!')
elif sign == 'pow':
    print(number_1 ** number_2)
elif sign == 'div':
    if number_2 != 0:
        print(number_1 // number_2)
    else:
        print('Деление на 0!')