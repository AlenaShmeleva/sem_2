# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def multiplier (num):
    list_multi = []
    multi = 2
    while num > 1:
        if num % multi == 0:
            list_multi.append(multi)
            num = num / multi
        else:
            multi += 1
    return list_multi

num = int(input("Введите число: "))

print(multiplier(num))