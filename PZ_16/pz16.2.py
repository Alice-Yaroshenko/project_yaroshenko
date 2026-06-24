"""
Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
переопределите методы, связанные с вычислением площади и периметра.
"""

class Figure:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f"Фигура: ширина = {self.width}, высота = {self.height}"


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)
    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}"

class Square(Figure):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
    def __str__(self):
        return f"Квадрат: сторона = {self.side}"

figure = Figure(5, 10)
print(figure)
print(f"Площадь: {figure.area()}")
print(f"Периметр: {figure.perimeter()}")

rectangle = Rectangle(7, 4)
print(rectangle)
print(f"Площадь: {rectangle.area()}")
print(f"Периметр: {rectangle.perimeter()}")

square = Square(6)
print(square)
print(f"Площадь: {square.area()}")
print(f"Периметр: {square.perimeter()}")
