# Составить функцию, которая выполнит суммирования числового ряда.


def sum_natural(n):
    s = 0
    i = 1
    while i <= n:
        s = s + i
        i = i + 1
    return s
