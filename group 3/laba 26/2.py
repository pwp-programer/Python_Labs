from random import randint
import numpy as np

n = int(input("Введите размер матрицы: "))

matrix = np.array([[randint(0, 9) for _ in range(n)] for _ in range(n)])

for row in matrix:
    print(row)

for i in range(n):
    for j in range(n):
        if i == j and i != 0:
            a = matrix[i][j-1]
            b = matrix[i-1][j]
            matrix[i][j-1] = matrix[i-1][j] = (a + b)/2

print('------------------------')

for row in matrix:
    print(row)