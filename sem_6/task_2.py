# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. 

def multi(numb):
    final_list = [i for i in range(20, numb + 1) if i % 20 == 0 or i % 21 == 0]
    return final_list

print(multi(int(input("Введите количство элементов списка: "))))
