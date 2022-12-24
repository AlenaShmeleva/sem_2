 # Напишите программу, удаляющую из текста все слова, содержащие "абв". 
 # В тексте используется разделитель пробел.

from random import choice

def input_list(numb: int):
    list = []
    abc = ['абв', 'вба', 'авб', 'ваб', 'бав', 'бва', 'бав']
    for i in range(numb):
        list.append("".join(choice(abc)))
    return " ".join(list)

def result_list(list: str):
    return " ".join(list.replace('абв', '').split())

list = input_list(int(input("Введите количество элементов:" )))
print(list)
print(result_list(list))