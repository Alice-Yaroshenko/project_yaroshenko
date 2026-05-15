"""
Составить генератор (yield), который преобразует все буквенные символы в заглавные
"""

def to_upper_generator(text):
    for symbol in text:
        if symbol.isalpha():
            yield symbol.upper()
        else:
            yield symbol

text = input("Введите текст: ")
for i in to_upper_generator(text):
    print(i, end="")
