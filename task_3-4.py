# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.


digits = set('0123456789')
i = 0
multiplier = ''
decrypted = ''

with open('task222.txt') as in_f_obj:
    string = in_f_obj.readline().strip()

char = string[i]
i += 1

while i < len(string):

    while string[i] in digits:
        multiplier += string[i]
        i += 1
        if i > (len(string) - 1):
            break

    # print(char * int(multiplier), end='')
    decrypted += (char * int(multiplier))

    multiplier = ''
    if i > (len(string) - 1):
        break
    char = string[i]

    i += 1

with open('answer22.txt', 'w') as out_f_obj:
    out_f_obj.write(decrypted)


# Напишите программу, которая считывает текст из файла
# (в файле может быть больше одной строки) и выводит самое частое
# слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое
# (можно использовать оператор < для строк).

dictionary = {}

with open('dataset_3363_3.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.lower()
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 1
            elif word in dictionary:
                dictionary[word] += 1

max_quantity = 1

for key, value in dictionary.items():
    current_quantity = dictionary[key]
    if current_quantity > max_quantity:
        max_quantity = current_quantity
        word_with_max_quantity = key

with open('dataset_3363_3333.txt', 'w') as out_f_obj:
    most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
    out_f_obj.write(most_popular)


# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает исходный файл с подобной структурой
# и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
#
# Также вычислите средние баллы по математике,
# физике и русскому языку по всем абитуриентам и добавьте полученные значения,
# разделённые пробелом, последней строкой в файл с ответом.

math_values = []
physics_values = []
russian_values = []
with open('dataset_3363_4.txt', 'r') as in_file:
    for line in in_file:
        current_line = line.strip().split(';')
        math_values.append(int(current_line[1]))
        physics_values.append(int(current_line[2]))
        russian_values.append(int(current_line[3]))
out_file = open('statistic.txt', 'w')
for i in range(len(math_values)):
    out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
if len(math_values) > 0:
    out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                   str(sum(physics_values) / len(physics_values)) + ' ' +
                   str(sum(russian_values) / len(russian_values)))
out_file.close()