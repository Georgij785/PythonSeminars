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


class my_matrix:
    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        self.row = [0] * self.columns

        self.matrix = [self.row] * self.rows
        for i in range(self.rows + 1):
            self.row = [0] * self.columns
            for j in range(self.columns):
                self.row[j] = (random.randint(-5, 10))
            self.matrix[i - 1] = self.row

    def __str__(self):
        result = ""
        for n in range(self.rows):
            self.Strrows = "["
            for m in range(self.columns):
                self.Strrows += f"{self.matrix[n][m]} ,"
            self.Strrows += "]"
            result += self.Strrows + "\n"
        return result

    def __add__(self, other):
        rowsOther = len(other.matrix)
        columnsOther = len(other.matrix[0])
        resrow = [0] * max(columnsOther, self.columns)
        resMatrix = my_matrix(max(self.rows, rowsOther), max(columnsOther, self.columns))
        for i in range(len(resMatrix.matrix)):
            resrow = [0] * len(resrow)
            for j in range(len(resMatrix.matrix[0])):
                if (i + 1 > len(self.matrix) or j + 1 > len(self.matrix[0])):
                    if i + 1 > len(other.matrix) or j + 1 > len(other.matrix[0]):
                        resrow[j] = 0
                    else:
                        resrow[j] = other.matrix[i][j]
                elif (i + 1 > len(other.matrix) or j + 1 > len(other.matrix[0])):
                    if i + 1 > len(self.matrix) or j + 1 > len(self.matrix[0]):
                        resrow[j] = 0
                    else:
                        resrow[j] = self.matrix[i][j]
                else:
                    resrow[j] = self.matrix[i][j] + other.matrix[i][j]
            resMatrix.matrix[i] = resrow
        return resMatrix


mar_1 = my_matrix(2, 8)
print(mar_1)
mar_2 = my_matrix(3, 6)
print(mar_2)
print(mar_1 + mar_2)
