"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        self.matrix = {}
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(random.randint(-5, 10))
            self.matrix[i]=row
            row.clear()

    # def __str__(self):
    #     result = ""
    #     print(self.columns)
    #     print(self.rows)
    #     for n in range(self.rows):
    #         rows = str()
    #         for m in range(self.columns):
    #             print(self.matrix[m][n])
    #             print(n,m)
    #             # rows += f"{self.matrix[m][n]} "
    #         # print(rows)
    #
    #         result += rows + "\n"
    #     return result


mar = Matrix(3, 3)
print(mar.matrix[1][0])
# print(a)