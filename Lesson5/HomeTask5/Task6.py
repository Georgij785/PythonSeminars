"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random
def game_binary(x, count=1):
    if count == 11:
        print("вы проиграли")
        return
    else:
        y = int(input("введите число > "))
        if y == x:
            print("верно, вы выйграли")
            return
        elif y > x:
            print("больше загадонного")
        else:
            print("меньше загадонного")
        count += 1
        game_binary(x, count)


x = random.randint(0, 100)
game_binary(x)