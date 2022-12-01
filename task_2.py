# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
N = int(input("Введите число: "))
num_list = []
factorial = 1
for i in range(1, N + 1):
    factorial *= i
    num_list.append(factorial)
print(num_list)