# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

from random import randint

def equation (k: int):
    with open("task_4.txt", "a", encoding="utf-8") as text:
        for i in range(k, 0, -1):
            text.write(f"{randint(-9, +10)}*x^{i}+")           
        text.write("\n")

for i in range(3):
    equation(int(input("Введите натуральную степень k (не меньше 3): ")))