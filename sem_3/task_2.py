# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def new_list(numbers):
    list_numbers = sample(range(1, numbers * 10), numbers)
    return list_numbers


def result(list_numbers):
    result_list = []
    for i in range(0, len(list_numbers)//2):
        result_list.append(list_numbers[i] * list_numbers[len(list_numbers)-1-i])
    print("Произведение пар:", result_list)


final_list = new_list(int(input(("Введите количество элементов: "))))
print(final_list)
result(final_list)