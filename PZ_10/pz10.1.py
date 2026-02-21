"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Количество элементов первого и второго файлов:
Индекс первого минимально элемента первого файла:
Индекс последнего максимального элемента второго файла:
Элементы кратные 4 первого и второго файлов:
"""

f1 = open("file1.txt", "w", encoding="utf-8")
nums1 = []

for i in range(10):
    n = random.randint(-50, 50)
    nums1.append(n)
    f1.write(str(n) + " ")
f1.close()

f2 = open("file2.txt", "w", encoding="utf-8")
nums2 = []
for i in range(12):
    n = random.randint(-50, 50)
    nums2.append(n)
    f2.write(str(n) + " ")
f2.close()

min1 = nums1[0]
index_min1 = 0
for i in range(len(nums1)):
    if nums1[i] < min1:
        min1 = nums1[i]
        index_min1 = i

max2 = nums2[0]
index_max2 = 0
for i in range(len(nums2)):
    if nums2[i] >= max2:   # >= чтобы получить ПОСЛЕДНИЙ максимум
        max2 = nums2[i]
        index_max2 = i

mult4_1 = []
for x in nums1:
    if x % 4 == 0:
        mult4_1.append(x)
mult4_2 = []
for x in nums2:
    if x % 4 == 0:
        mult4_2.append(x)

res = open("result.txt", "w", encoding="utf-8")
res.write("Элементы первого и второго файлов:\n")
res.write(str(nums1) + "\n")
res.write(str(nums2) + "\n\n")
res.write("Количество элементов первого файла: " + str(len(nums1)) + "\n")
res.write("Количество элементов второго файла: " + str(len(nums2)) + "\n\n")
res.write("Индекс первого минимального элемента первого файла: " + str(index_min1) + "\n")
res.write("Индекс последнего максимального элемента второго файла: " + str(index_max2) + "\n\n")
res.write("Элементы кратные 4 первого файла: " + str(mult4_1) + "\n")
res.write("Элементы кратные 4 второго файла: " + str(mult4_2))
res.close()


