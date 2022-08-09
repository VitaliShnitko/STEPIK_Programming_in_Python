# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
#
# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b] на все числа отрезка [c;d].
#
# Числа a, b, c и d являются натуральными и не превосходят 10, a ≤ b,a ≤ b.
#
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

a, b, c, d = int(input()), int(input()), int(input()), int(input())  # ввод данных#
print(" ")  # вывод пустой ячейки#
for i in range(c, d + 1):  # перебор первого ряда цифр#
    print("\t", i, end="")  # вывожу цифры(\t это отступ между цифрами)#
for i in range(a, b + 1):  # снова перебор,но уже второго#
    print('\n', i, end="")  # вывожу первою цифру#
    for j in range(c, d + 1):  # перебор второго#
        print('\t', i * j, end="")
