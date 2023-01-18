# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.


# digits = set('0123456789')
# i = 0
# multiplier = ''
# decrypted = ''
#
# with open('task222.txt') as in_f_obj:
#     string = in_f_obj.readline().strip()
#
# char = string[i]
# i += 1
#
# while i < len(string):
#
#     while string[i] in digits:
#         multiplier += string[i]
#         i += 1
#         if i > (len(string) - 1):
#             break
#
#     # print(char * int(multiplier), end='')
#     decrypted += (char * int(multiplier))
#
#     multiplier = ''
#     if i > (len(string) - 1):
#         break
#     char = string[i]
#
#     i += 1
#
# with open('answer22.txt', 'w') as out_f_obj:
#     out_f_obj.write(decrypted)


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



