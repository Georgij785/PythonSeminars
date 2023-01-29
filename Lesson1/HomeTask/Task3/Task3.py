"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = input("Введите ваше число > ")
number_two = int(number + number)
number_three = int(number + number + number)
number = int(number)
result = number + number_two + number_three
print(f"{number} + {number_two} + {number_three} = {result}")
