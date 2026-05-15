"""
Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
"""

import random
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [
    [random.randint(0, 20) for _ in range(cols)]
    for _ in range(rows)
  ]

print("Исходная матрица:")
for row in matrix:
    print(row)

new_matrix = [
    [0 if x > 10 else x for x in row]
    for row in matrix
  ]

print("\nИзменённая матрица:")
for row in new_matrix:
    print(row)
