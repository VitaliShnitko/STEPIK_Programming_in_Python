# Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
#
# Формат ввода, который используют Малевийцы:
# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника
# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника
# круг
# r
# где r — радиус окружности

figure = input()
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    square = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    print(square)


elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    square_kv = a * b
    print(square_kv)

elif figure == 'круг':
    r = int(input())
    square_kr = 3.14 * (r ** 2)
    print(square_kr)