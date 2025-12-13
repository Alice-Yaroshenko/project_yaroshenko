# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
# вывести TRUE, если нет — вывести FALSE.




N = int(input("Введите N (>0): "))

found = False
temp = N

while temp != 0:
    if temp % 10 == 2:
        found = True
    temp = temp // 10

if found:
    print("TRUE")
else:
    print("FALSE")
