# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.mat])

    def __add__(self, other):
        new_matrix = [
            [self.mat[i][j] + other.mat[i][j] for j in range(len(self.mat[0]))]
            for i in range(len(self.mat))]

        return Matrix(new_matrix)

matrix_1 = Matrix([[1, 1, 3], [1, 1, 2], [1, 2, 3], [2, 5, 1]])
matrix_2 = Matrix([[3, 2, 1], [2, 2, 2], [3, 1, 3], [4, 2, 3]])
print(matrix_1)
print('++++++' * 3)
print(matrix_2)
print('++++++' * 3)
matrix_3 = matrix_2 + matrix_1
print(matrix_3)