# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
my_list = [3, 45, 3, 34, 67, 5, 34, 5, 5, 34, 5, 3, 54, 3, 5, 34, 5]

# Вариант 1
my_list2 = my_list.copy()
set = set(my_list2)
print(set)

