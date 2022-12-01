# 3. Задайте список из n чисел, 
# заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input("Введите число: "))
sum = 0
num_list = []
for i in range(1, n + 1):
    num_list.append((1 + 1 /i) ** i)
    sum = sum + (1 + 1 /i) ** i
print(num_list)
print("Сумма чисел равна", sum)