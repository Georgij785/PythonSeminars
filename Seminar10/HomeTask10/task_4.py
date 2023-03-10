"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list=["разработка", "администрирование", "protocol","standard"]
b_list=[]
for i in my_list:
    a=i.encode()
    print(a)
    b_list.append(a)
print("\n")
for y in b_list:
    s=y.decode()
    print(s)