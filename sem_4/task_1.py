# 1. Вычислить число c заданной точностью d 

from decimal import Decimal

def calculation (num, d):
    res = Decimal(f'{num}').quantize(Decimal(f'{d}'))
    return res

num = float(input("Введите число: "))
d = float(input("Введите заданную точность по примеру 0.0001: "))

print(calculation(num, d))