# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
from random import randint

def new_list(nums):
    list_nums = []
    for i in range(1, nums+1):
        list_nums.append(randint(1,10))
    return list_nums

def result(list_nums: list):
    result_list = []
    for i in list_nums:
        if i not in result_list:
            result_list.append(i)
        else:
            result_list.remove(i)
    return result_list


first_list = new_list(int(input("Введите количество элементов последовательности: ")))
print(first_list)
print(result(first_list))