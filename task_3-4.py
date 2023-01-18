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



