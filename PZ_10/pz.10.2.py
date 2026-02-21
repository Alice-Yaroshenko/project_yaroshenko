"""
Из предложенного текстового файла (text18-30.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно поставив после последней строки автора и название
произведения.
"""

f = open("text18-30.txt", "r", encoding="utf-8")
text = f.read()
f.close()

print("Содержимое файла:\n")
print(text)

punct = ",.:;!?-"
count = 0
for ch in text:
    if ch in punct:
        count += 1
print("\nКоличество знаков препинания:", count)

lines = text.split("\n")
newf = open("poem_result.txt", "w", encoding="utf-8")
for line in lines:
    newf.write(line + "\n")
  
newf.write("\nМ. Ю. Лермонтов\n")
newf.write("Бородино")
newf.close()
