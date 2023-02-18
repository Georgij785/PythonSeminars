'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше
заданного минимума и не больше заданного максимума)
'''
import random

my_list = [i for i in range(1, 100)]
indexes = []


def borders(numbers_list, min_v, max_v, indexes, c):
    if c == len(numbers_list):
        return
    else:
        if numbers_list[c] >= min_v and numbers_list[c] <= max_v:
            indexes.append(c)
        borders(numbers_list, min_v, max_v, indexes, c + 1)


borders(my_list, 10, 15, indexes, 0)
print(indexes)
