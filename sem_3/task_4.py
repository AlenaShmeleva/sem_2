# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

from random import uniform

def new_list(numbers):
    list_numbers = []

    for i in range(numbers):
        list_numbers.append(round(uniform(1, numbers), 2))

    return list_numbers


def find_min_max(list_numbers):
    min = max = round(list_numbers[0] % 1, 2)
    for i in range(1, len(list_numbers)):
        numbers = round(list_numbers[i] % 1, 2)
        if numbers < min:
            min = numbers
        elif numbers > max:
            max = numbers
    print("Разница между min и max дробной части равна", max - min)
    

final_list = new_list(int(input(("Введите количество элементов: "))))
print(final_list)
find_min_max(final_list)