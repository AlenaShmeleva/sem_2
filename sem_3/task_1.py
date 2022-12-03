# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def new_list(numbers):
    list_numbers = sample(range(1, numbers * 10), numbers)
    return list_numbers


def summa(list_numbers):
    summa_numb = 0
    for i in range(0, len(list_numbers), 2):
        summa_numb += list_numbers[i]
    print("Сумма элементов равна", summa_numb)


final_list = new_list(int(input(("Введите количество элементов: "))))
print(final_list)
summa(final_list)