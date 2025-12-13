# Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся
# в списке, на исходное значение первого четного числа. Если четные числа в списке# 
# отсутствуют, то оставить список без изменений.


import random

def process_list():
    try:
        N = int(input("Введите размер списка N: "))
        if N <= 0:
            print("Размер списка должен быть положительным")
            return
        
        numbers = []
        i = 0
        while i < N:
            numbers.append(random.randint(1, 100))
            i += 1
        
        print(f"\nИсходный список: {numbers}")
        
        first_even = None
        i = 0
        while i < N:
            if numbers[i] % 2 == 0:
                if first_even is None:
                    first_even = numbers[i]
                i += 1
            else:
                i += 1
        
        if first_even is not None:
            i = 0
            while i < N:
                if numbers[i] % 2 == 0:
                    numbers[i] += first_even
                i += 1
        
        print(f"Результат: {numbers}")
        
    except ValueError:
        print("Ошибка! Введите целое число")

process_list()
