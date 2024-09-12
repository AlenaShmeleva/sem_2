# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def binary_numb(numb):
    new_numb = []

    while numb > 0:
        new_numb.insert(0, numb % 2)
        numb //= 2

    print(*new_numb, sep="")

binary_numb(int(input("Введите число: ")))