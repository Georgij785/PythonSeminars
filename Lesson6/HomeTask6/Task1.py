'''
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести
с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''


def create_numbers(a, n, d, my_numders, c):
    if len(my_numders) > n:
        return
    else:
        my_numders.append(a + (c) * d)
        create_numbers(a, n, d, my_numders, c + 1)
    return my_numders


my_list = []
print(create_numbers(int(input("Введите первое число > ")), int(input("Введите колличество чисел в последовательности > ")), int(input("Введите шаг между числами > ")), my_list, 0))
