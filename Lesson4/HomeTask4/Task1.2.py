# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())
i = 2
my_list = []
while n != 1:
    while n % i == 0:
        n = n // i
        my_list.append(i)
    i += 1
print(my_list)
