# Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки,
# которая выводит все позиции, на которых встречается число xx в переданном списке lst.
#
# Позиции нумеруются с нуля, если число xx не встречается в списке,
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
#
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
#
lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
    if x == lst[i]:
        print(i, end=' ')

if x not in lst:
    print('Отсутствует')