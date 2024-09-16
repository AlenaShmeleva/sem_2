# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента.

from random import randint

def max_el(numb):
    list = [randint(1, 500) for _ in range(numb)]
    print(list)
    final_list = [list[numb] for numb in range(1, len(list)) if list[numb] > list[numb - 1]]
    return final_list

print(max_el(int(input("Введите количство элементов списка: "))))