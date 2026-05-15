"""
В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
"""
import random

n = int(input("Введите размер матрицы: "))

matrix = [
    [random.randint(1, 10) for _ in range(n)]
    for _ in range(n)
  ]

print("Исходная матрица:")
for row in matrix:
    print(row)

new_matrix = [
    [
        matrix[i][j] if i == j else matrix[i][j] * 2
        for j in range(n)
    ]
    for i in range(n)
  ]

print("\nИзменённая матрица:")
for row in new_matrix:
    print(row)
