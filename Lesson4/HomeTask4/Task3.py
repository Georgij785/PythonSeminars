'''
    Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

    Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

k = int(input())

number = []
for i in range(1, 100):
    number.append(random.randint(1, 100))
number_final = ""
a = k
for item in range(k):
    number_final += f"{number[item]}x^{a}+"
    a -= 1
y = random.randint(0, 100)
number_final += str(number[y])
print(number_final)
