"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
a=b"class"
b=b"function"
c=b"method"

my_list=list()
my_list.append(a)
my_list.append(b)
my_list.append(c)
for i in my_list:
    print(type(i))
    print(i)
    print(len(i))
