'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и
посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру,
чтобы убрать пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text.
Если результат работы скрипта не принимается, проверьте поле url на правильность.
Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.
'''

import requests

with open('dataset_33711111.txt') as in_f_obj:
    url = in_f_obj.read().strip()

r = requests.get(url)
counter = 0

for line in r.text.splitlines():
    counter += 1

with open('out_dataset_3378_002.txt', 'w') as out_f_obj:
    out_f_obj.write((str(counter)))



'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''

import  requests

link = "https://stepic.org/media/attachments/course67/3.6.3/"

with open('dataset_3378_3.txt') as inf:
    t = inf.readline().strip()

t = str(requests.get(t).text)

while 'we' not in t:
    print(t)
    t = requests.get(link + t).text
print(t)
